#!/usr/bin/env python
import sys

COL_TYPES = ['likes', 'retweets', 'Twitter Web App', 'Twitter for Android', 'Twitter for iPhone']
KIND_BIDEN = "Joe_Biden"
KIND_TRUMP = "Donald_Trump"
KIND_BOTH = "Both_Candidates"
SEPARATOR = '|---|'

kind_dict = {
    KIND_BOTH: {item: 0 for item in COL_TYPES},
    KIND_TRUMP: {item: 0 for item in COL_TYPES},
    KIND_BIDEN: {item: 0 for item in COL_TYPES},
}

for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    kind, likes, retweets, source = line.split(SEPARATOR)
    likes = int(float(likes))
    retweets = int(float(retweets))

    if source in kind_dict[kind]:
        kind_dict[kind][source] += 1
    kind_dict[kind]['likes'] += likes
    kind_dict[kind]['retweets'] += retweets

print("################", " ".join(COL_TYPES))
for kind, cols_dict in kind_dict.items():
    cols_str = ' '.join(map(str, cols_dict.values()))
    print(kind, cols_str)