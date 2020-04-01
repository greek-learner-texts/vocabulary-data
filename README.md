# vocabulary-data

consolidating vocabulary data relevant to the Greek Learner Texts Project


## Sources

These GitHub repositories:

* https://github.com/jtauber/core-gnt-vocab
* https://github.com/jtauber/greek-lemma-mappings
* https://github.com/morphgnt/morphological-lexicon
* https://github.com/jtauber/major80/ (private)

and this spreadsheet:

* https://docs.google.com/spreadsheets/d/1ke7JuFd5iy7bPSCHutgRYFvjDbcSScABld4zwEvDb-s/edit?usp=sharing


## Terminology

We use the term **lexeme**, **entry**, **lexical item**, **vocabulary item** or just **item** to refer to the object being distinguished including all its properties.

We use the term **lemma**, **headword**, **dictionary form**, **citation form**, or just **key** to refer to the string that identifies the lexical item.


## Categories of Data

* We just have an unordered list of items with no additional properties (so effectively just the keys)

* we have an unordered list of items but they contain additional properties (perhaps a gloss, part-of-speech, inflectional class, semantic domain, etc)

* we have some mapping between the items in two lists which might differ in the key used in each list

* we have corpus-specific frequency information on each item

* we have ordering (either explict in the data or based on sorted on some property whether it be lexicographical sorting of the key or ordering based on frequency in a particular corpus)
