# Prior work

## Australian Ecosystems Modelling Framework: 
https://research.csiro.au/biodiversity-knowledge/projects/models-framework/

Recognises the _dynamic_ nature of ecosystems, under natural conditions, that provide a consistent flow of services.

## IUCN Global Ecosystem Typology: 
https://global-ecosystems.org/

The recommended typology for reporting ecosystems accounts under the **SEEA framework** and has been **used in Europe and the US** for this purpose.

## NVIS: 
https://www.environment.gov.au/land/native-vegetation/national-vegetation-information-system

Established and probably the most comprehensive source of information on Australian ecosystem extent

## LCCS: 
https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/category/details/en/c/1036361/

The GA Digital Earth Australia LCCS data is used as the **basis for reporting SEEA land accounts**. Ecosystem accounts (in Glenn's view) should at least consider the relationship between land cover and ecosystem extent.

## ENVO:
https://sites.google.com/site/environmentontology/home

Ontology for environmental systems, entities and properties. 
Part of the [OBO Foundry](http://obofoundry.org/) - a consistent system of biomedical ontologies. The following are some potential starting points: 

- [aquatic ecosystem](http://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001787)
- [terrestrial ecosystem](https://www.ebi.ac.uk/ols/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001790)
- [wetland ecosystem](https://www.ebi.ac.uk/ols/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001209&lang=en&viewMode=All&siblings=false)

OBO ontologies follow a consistent _genus-differentia_ pattern for subclassing, of the form 
- An **X** is a **G** that **D**
- G should be in the same ontology
- D is discriminating characteristics that differentiate Xs from _other_ Gs

See https://philpapers.org/archive/SEPGFW.pdf for the gory detail 

Note that a class _may_ be a sub-class of more than one parent class, implying that the intersection of the parent classes is non-empty
