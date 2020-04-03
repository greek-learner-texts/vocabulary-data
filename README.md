# vocabulary-data

consolidating vocabulary data relevant to the Greek Learner Texts Project


## Sources

These GitHub repositories:

* https://github.com/jtauber/major80/ (private) — now fully incorporated in to `raw/` directory
* https://github.com/morphgnt/morphological-lexicon
* https://github.com/morphgnt/data-cleanup (private)
* https://github.com/jtauber/core-gnt-vocab
* https://github.com/jtauber/greek-lemma-mappings
* https://github.com/jtauber/lsj-headwords (private)

and this spreadsheet:

* https://docs.google.com/spreadsheets/d/1ke7JuFd5iy7bPSCHutgRYFvjDbcSScABld4zwEvDb-s/edit?usp=sharing

and also:

* https://github.com/dcthree/ancient-greek-lexica
* https://github.com/translatable-exegetical-tools/Abbott-Smith
* https://github.com/openscriptures/GreekResources

The raw data from these sources can be found in `raw/`.


## Terminology

We use the term **lexeme**, **entry**, **lexical item**, **vocabulary item** or just **item** to refer to the object being distinguished including all its properties.

We use the term **lemma**, **headword**, **dictionary form**, **citation form**, or just **key** to refer to the string that identifies the lexical item.

Sometimes a distinction is made between the bare form used as a lemma (e.g. λόγος) and the full headword or citation form (e.g. λόγος, ου, ὁ). There are also cases where a numeral or gloss is added to distinguish homographs.

Also see [Linking Lexical Resources for Biblical Greek](https://vimeo.com/243936959) for a talk from SBL 2017 on additional issues and concepts.


## Categories of Data

* We just have an unordered list of items with no additional properties (so effectively just the keys).

* We have an unordered list of items but they contain additional properties (perhaps a gloss, part-of-speech, inflectional class, semantic domain, etc).

* We have some mapping between the items in two lists which might differ in the key used in each list.

* We have corpus-specific frequency information on each item.

* We have ordering (either explicit in the data or based on sorted on some property, whether it be lexicographical sorting of the key or ordering based on frequency in a particular corpus, or something else).
