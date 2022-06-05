#!/usr/bin/env python
import sys

KIND_BIDEN = "Joe_Biden"
KIND_TRUMP = "Donald_Trump"
KIND_BOTH = "Both_Candidates"
KIND_TYPES = [KIND_BIDEN, KIND_TRUMP, KIND_BOTH, "ALL"]
SEPARATOR = '|---|'

state_dict = {
    'New York': {item: 0 for item in KIND_TYPES},
    "Texas": {item: 0 for item in KIND_TYPES},
    "California": {item: 0 for item in KIND_TYPES},
    "Florida": {item: 0 for item in KIND_TYPES},
}

for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    kind, state = line.split(SEPARATOR)

    if state in state_dict:
        state_dict[state]["ALL"] += 1
        state_dict[state][kind] += 1

print("################", " ".join(KIND_TYPES))
for state, kinds_dict in state_dict.items():
    kinds_dict: dict
    all_docs_count = kinds_dict.pop("ALL")
    kinds_percentages = ' '.join(map(lambda x: str(x / all_docs_count) if all_docs_count != 0 else '0', kinds_dict.values()))
    print(state, kinds_percentages, all_docs_count)
