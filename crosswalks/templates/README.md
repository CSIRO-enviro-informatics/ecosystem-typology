# Crosswalk template

[This Excel template](classifier-crosswalk-sssom-template.xlsx) is provided to support the development and recording of crosswalks between classifier systems.

The template follows [A Simple Standard for Sharing Ontological Mappings (SSSOM)](https://github.com/mapping-commons/sssom).
The columns in the template are a subset of the [slots provided by SSSOM](https://mapping-commons.github.io/sssom/Mapping/).
The [ordering of the columns must not be changed](https://mapping-commons.github.io/sssom/spec/#tsv).
[`status` is a new slot](https://github.com/mapping-commons/sssom/issues/345) proposed to manage lifecycle recording. 

## Explanation and Example

### Scope of crosswalk

Each crosswalk should be between _one source_ and _one target_ classification system.

### Structure of a mapping

Each mapping within a crosswalk is denoted by

- a term from the source - called the _subject_
- a term from the target - called the _object_
- a term indicating the nature of the correspondence - called the _predicate_

### Terms are denoted by URIs

Each term **must** be denoted by a web-identifier or "URI".
The URI may be given as

- a full URI - e.g.

```
<https://global-ecosystems.org/explore/groups/MFT1.3>

<http://www.w3.org/2004/02/skos/core#closeMatch>
```

- or (preferred) in compact form, where the URI-stem is replaced with a prefix or alias - e.g.

```
get:groups/MFT1.3

skos:closeMatch
```

Make sure to record the prefix&rarr;URI-stem map in the `header` sheet corresponding to the crosswalk, e.g.

```
get: https://global-ecosystems.org/explore/

skos: http://www.w3.org/2004/02/skos/core#
```

The sheet also has a column for the `_label` for each of the subject, object, and author, to allow you to get started even if you don't yet have the term URI or author ORCID.

### Mapping lifecycle

An example sheet is provided in the template file. It records the complete lifecycle for two (notional) mappings, from proposal through review, acceptance to publication.
Note that **all rows in a set representing a single mapping have the same values in these first six columns** -

| subject_id | subject_label | predicate_id |  object_id | object_label | mapping_justification |
| -- | -- | -- | -- | -- | -- |

It is useful but not essential to have the complete lifecycle recorded.
But if only part of the lifecycle is available, then only record that part.

For example, for an existing crosswalk that has already been published then just record the final set of mappings with the status `status:published`.
Or if the crosswalk is only at an early stage of development, the status values will be `status:draft` and `status:submitted`. 

### Further mappings

Further mappings between other terms in the same pair of classification systems can be recorded on the same sheet, following the same pattern.
Each mapping lifecycle will have a _different_ but _consistent_ set of values in the first six columns.

### Controlled fields

A validation rule in the spreadsheet provides a drop-down list in the following columns to select the values from a controlled list:

| ...  | predicate_id | ... | mapping_justification | ... | status | ... |
| -- | -- | -- | -- | -- | -- | -- |

(The lists are on additional sheets in the template.)

## Pre-requisites

For each crosswalk:

1. one source and one target classification system
1. subject-matter expert(s)
   1. to develop the mappings
   1. to review the mappings
1. the [ORCID identifier](https://orcid.org/) for each person involved in developing and publishing the crosswalk
1. a stable URI for each term in both classification systems
   - try looking in [Research Vocabularies Australia (RVA)](https://vocabs.ardc.edu.au/)

Note that in [RVA](https://vocabs.ardc.edu.au/) the URL for the web-page showing the details for a term, such as:

```
<https://vocabs.ardc.edu.au/repository/api/lda/abares/australian-land-use-and-management-classification/version-8/resource?uri=http%3A%2F%2Fwww.neii.gov.au%2Fdef%2Fvoc%2FACLUMP%2Faustralian-land-use-and-management-classification%2FMarsh-or-wetlandsaline>
```

is _not_ the term URI, which is shown at the top of the page

```
<https://linked.data.gov.au/def/alum/Marsh-or-wetlandsaline>
```

or in compact form

```
alum8:Marsh-or-wetlandsaline
```

where

```
alum8: https://linked.data.gov.au/def/alum/
```
