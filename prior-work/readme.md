# Prior work

## Australian Ecosystems Modelling Framework

[https://research.csiro.au/biodiversity-knowledge/projects/models-framework/](https://research.csiro.au/biodiversity-knowledge/projects/models-framework/)

Recognises the _dynamic_ nature of ecosystems, under natural conditions, that provide a consistent flow of services.

## Australian Land Use and Management classification (ALUM)

The Australian Land Use and Management (ALUM) Classification system provides a nationally consistent method to collect and present land use information for a wide range of users across Australia. The latest version (Version 8) of the classification conforms to the Australian Spatial Data Infrastructure (ASDI) standard for land use datasets and is also available as an environmental vocabulary service or glossary.

[ALUM Version 8](https://www.agriculture.gov.au/abares/aclump/land-use/alum-classification)

[Mapping from ALUM8 &rarr; IUCN GET](https://github.com/CSIRO-enviro-informatics/ecosystem-typology/files/13446193/ALUMv8.xlsx)

## VAST / AquaVAST

Thackway

- I: Residual
- II: Modified
- III(a): Transformed
- III(b): Transformed
- IV: Replaced-Adventive
- V: Replaced-Managed
- VI: Removed

## IUCN Global Ecosystem Typology

[https://global-ecosystems.org/](https://global-ecosystems.org/)
- [Source Paper](https://www.nature.com/articles/s41586-022-05318-4)

The recommended typology for reporting ecosystems accounts under the [SEEA framework](https://seea.un.org/ecosystem-accounting/) and has been **used in Europe and the US** for this purpose.

## NVIS

[https://www.environment.gov.au/land/native-vegetation/national-vegetation-information-system](https://www.environment.gov.au/land/native-vegetation/national-vegetation-information-system)

Established and probably the most comprehensive source of information on Australian ecosystem extent

## LCCS

[https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/category/details/en/c/1036361/](https://www.fao.org/land-water/land/land-governance/land-resources-planning-toolbox/category/details/en/c/1036361/)

The GA Digital Earth Australia LCCS data is used as the **basis for reporting SEEA land accounts**. Ecosystem accounts (in Glenn's view) should at least consider the relationship between land cover and ecosystem extent.

## ENVO

[https://sites.google.com/site/environmentontology/home](https://sites.google.com/site/environmentontology/home)

Ontology for environmental systems, entities and properties.
Part of the [OBO Foundry](http://obofoundry.org/) - a consistent system of biomedical ontologies. The following are some potential starting points:

- [biome](http://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_00000428)
- [aquatic ecosystem](http://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001787)
- [terrestrial ecosystem](https://www.ebi.ac.uk/ols/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001790)
- [wetland ecosystem](https://www.ebi.ac.uk/ols/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001209&lang=en&viewMode=All&siblings=false)

OBO ontologies follow a consistent _genus-differentia_ pattern for subclassing, of the form

- An **X** is a **G** that **D**
- G should be in the same ontology
- D is discriminating characteristics that differentiate Xs from _other_ Gs

See [Guidelines for writing definitions in ontologies](https://philpapers.org/archive/SEPGFW.pdf) for the gory detail

Note that a class _may_ be a sub-class of more than one parent class, implying that the intersection of the parent classes is non-empty.
For example, [biome](http://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_00000428) is a subclass of both [system](http://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FRO_0002577)/[ecosystem](http://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001110) and [object](http://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBFO_0000030)/[biosphere](http://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000817)
