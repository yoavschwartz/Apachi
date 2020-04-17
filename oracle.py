#!/usr/bin/python
# coding=utf-8

import sys

p = [[], [], [], [], []]

lines = sys.stdin.readlines()
lemma = sys.argv[1]

excluded_lemmas = [
    'paper_accepted_verifiability_soundness_2_true_no_adversary',
    'paper_rejected_verifiability_soundness_2_true_no_adversary',
    'key_secret',
    'paper_secrecy_accepted',
    'paper_secrecy_rejected',
    'review_secrecy',
]


for line in lines:
    num = line.split(':')[0]
    if lemma not in excluded_lemmas:
        if 'pc_privk' in line:
            p[0].append(num)
        else:
            p[3].append(num)
    elif 'paper_secrecy_rejected' in lemma:
        if 'privk' in line:
            p[0].append(num)
        else:
            p[3].append(num)
    else:
        p[0].append(num)

for goal in [item for sublist in p for item in sublist]:
    print(goal)
