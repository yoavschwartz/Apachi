#!/usr/bin/python
# coding=utf-8

import sys

p = [[], [], [], [], []]

lines = sys.stdin.readlines()
lemma = sys.argv[1]

for line in lines:
    num = line.split(':')[0]
    if 'pc_privk' in line:
        p[0].append(num)
    elif 'review_authenticity' in lemma:
        if 'reviewer_privk' in line:
            p[1].append(num)
        elif 'privk' in line:
            p[2].append(num)
    else:
        p[3].append(num)

for goal in [item for sublist in p for item in sublist]:
    print(goal)
