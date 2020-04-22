#!/usr/bin/env python3

import collections
import re
import sys
import unicodedata

from greek_accentuation.characters import strip_length


def nfc(s):
    return unicodedata.normalize("NFC", s)


def convert(headword):
    headword = strip_length(headword)
    headword = re.sub("^\d\. ", "", headword)
    headword = re.sub("^\*", "", headword)

    if "(" in headword:
        return [
            nfc(re.sub(r"\([^\)]+\)", "", headword)),
            nfc(re.sub(r"[\(\)]", "", headword)),
        ]
    elif " or " in headword:
        alt1, alt2 = headword.split(" or ")
        return [nfc(alt1), nfc(alt2)]
    elif " and " in headword:
        alt1, alt2 = headword.split(" and ")
        return [nfc(alt1), nfc(alt2)]
    else:
        return [nfc(headword)]



GE = []
for line in open("raw/ge-headwords.txt"):
    my_num, headword = nfc(line).strip().split(maxsplit=1)
    GE.append((headword, my_num))

GE2 = collections.defaultdict(list)
for line_num, line in enumerate(open("raw/ge-dcthree.csv"), 1):
    ge_id, duke_headword = nfc(line).strip().split(",")
    ge_id = int(ge_id)
    GE2[ge_id].append(duke_headword)
    my_headword, my_num = GE[ge_id - 1]
    # print(ge_id, duke_headword, convert(my_headword), my_headword, my_num, line_num, sep="\t")
    if duke_headword not in convert(my_headword):
        print("@@@", file=sys.stderr)
        break

SEP1 = "\t"
SEP2 = "|"

for ge_id, entry in enumerate(GE, 1):
    headword, my_num = entry
    if my_num == "?":
        my_num = ""
    if ge_id in GE2:
        if convert(headword) != GE2[ge_id]:
            print("@@@", headword, convert(headword), GE2[ge_id])
            quit()
        assert SEP1 not in headword
        assert SEP2 not in headword
        assert SEP1 not in "".join(GE2[ge_id])
        assert SEP2 not in "".join(GE2[ge_id])
        print(ge_id, headword, SEP2.join(GE2[ge_id]), my_num, sep=SEP1)
    else:
        assert SEP1 not in headword
        assert SEP2 not in headword
        print(ge_id, headword, "", my_num, sep=SEP1)
