# RDF representation of IUCN GET

RDF implementation of the IUCN Global Ecosystem Typology v2.1, levels 1-3 

Each Realm, Biome and Functional Group is implemented as an SKOS Concept. 
SKOS 'has broader' is used to organize the IUCN hierarchy. 
The classification levels are managed using XKOS. 

The baseURI is currently set to https://w3id.org/env/iucn-get/ however this is merely a placeholder.