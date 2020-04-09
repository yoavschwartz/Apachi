#!/usr/bin/python
# coding=utf-8

import sys

p = [[], [], [], []]

lines = sys.stdin.readlines()
lemma = sys.argv[1]

for line in lines:
    num = line.split(':')[0]

    # if lemma == 'paper_accepted_verifiability_soundness_1_exists_trace_where_false':
    #     if any(string in line for string in ['!PC(']):
    #         p[0].append(num)
    #     elif any(string in line for string in ['Ready_']):
    #         p[1].append(num)
    #     elif any(string in line for string in ['!PC', 'Make']):
    #         p[2].append(num)
    #     else:
    #         p[3].append(num)

    # else:
    p[3].append(num)


for goal in [item for sublist in p for item in sublist]:
    print(goal)
