import pandas as pd
import rdfpandas
import rdflib
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager
# from rdflib.namespace import RDF
from rdflib import Literal, URIRef

crosswalk_name = 'Coastal-IUCNGET'  # set this before running 
crosswalk_dir = 'Coastal-IUCNGET' + '/' # tweak this before running when necessary
crosswalk_xlsx = crosswalk_name + '.xlsx'
# crosswalk_url = 'https://github.com/CSIRO-enviro-informatics/ecosystem-typology/raw/main/crosswalks/' + crosswalk_name + '/' + crosswalk_xlsx # uses Excel file from GitHub
crosswalk_url = './crosswalks/' + crosswalk_dir + crosswalk_xlsx # uses local copy of excel file
crosswalk_sheet = 'SSSOM'
header_sheet = 'header'

crosswalk_json = crosswalk_name + '.json'
crosswalk_ttl = crosswalk_name + '.ttl'
outformat_index = 0  # choose this before running
output_format = ['turtle', 'json-ld'][outformat_index]
output_file = [ './crosswalks/' + crosswalk_ttl , './crosswalks/' + crosswalk_json ][outformat_index]

# Read the crosswalk into a table
crosswalk_df = pd.read_excel(crosswalk_url, sheet_name=crosswalk_sheet)
# print(crosswalk_df, '\n')

# Read the header into a table of prefixes and URIs
header_df = pd.read_excel(crosswalk_url, sheet_name=header_sheet, header=None, names=['prefix', 'URI'])
header_df[['prefix', 'URI']] = header_df['prefix'].str.split(': ', expand=True)
header_df['prefix'] = header_df['prefix'].str.strip()

namespace_manager = NamespaceManager(Graph())
# Bind the prefixes to the graph
for i in range(len(header_df)):
    namespace_manager.bind(header_df.prefix[i], Namespace(header_df.URI[i]))

map_ns = namespace_manager.store.namespace("map")
sssom_ns = namespace_manager.store.namespace("sssom")
subj_list = []
rdf_type = []
for idx in crosswalk_df.index:
    subj_list.append(f"{map_ns}{str(idx+1)}")
    rdf_type.append(f"{sssom_ns}Mapping")
crosswalk_df.insert(0, 'subject_uri', subj_list, True)
crosswalk_df.insert(1, 'rdf:type', rdf_type, True)
crosswalk_df = crosswalk_df.reset_index().set_index('subject_uri')
crosswalk_df.drop(columns=['index'], inplace=True)
# Convert crosswalk dataframe to RDF graph
graph = rdfpandas.to_graph(crosswalk_df, namespace_manager)

# # Serialize the RDF graph to Turtle format
serialized = graph.serialize(format=output_format)
print(serialized)

with open(output_file, 'wb') as file:
	file.write(serialized.encode('utf-8'))

