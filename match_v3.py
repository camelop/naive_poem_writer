from pace_statistic import *

before = {}
after = {}


def create_pair(x, y):
    # insert y
    if x in before:
        if y in before[x]:
            before[x][y] += 1
        else:
            before[x][y] = 1
    else:
        before[x] = {y: 1}
    # insert x
    if y in after:
        if x in after[y]:
            after[y][x] += 1
        else:
            after[y][x] = 1
    else:
        after[y] = {x: 1}


import random
import os


def findMatch(k_v):
    return k_v[1] / (math.log2(2 +
                               (c_5_8[k_v[0]] if k_v[0] in c_5_8 else 0) +
                               (c_7[k_v[0]] if k_v[0] in c_7 else 0)) ** 2)


def match(x):
    if x in before:
        list = sorted(before[x].items(),
                      key=findMatch,
                      reverse=True)
        '''
        for k_v in list:
            print(k_v[0], k_v[1] / (math.log2(2 +
                                              (c_5_8[k_v[0]] if k_v[0] in c_5_8 else 0) +
                                              (c_7[k_v[0]] if k_v[0] in c_7 else 0)) ** 2))
        assert(1 == 0)
        '''
        choose = list[random.randint(0, min(len(list) - 1, 20))]
        return choose[0], findMatch(choose)
    else:
        return "一"


# before - after
for p in p_5_8:
    nw = None
    for line in p.content:
        if nw is None:
            nw = line
        else:
            for i in range(5):
                create_pair(nw[i], line[i])
            nw = None

for p in p_7:
    nw = None
    for line in p.content:
        if nw is None:
            nw = line
        else:
            for i in range(7):
                create_pair(nw[i], line[i])
            nw = None

import math


def evaluate(line):
    ret = 0.0
    for i in range(len(line) - 1):
        word = line[i] + line[i + 1]
        if word in f_5_8:
            # print(math.log2(2 + f_5_8[word] / 100))
            ret += math.log2(2 + f_5_8[word] / 10)
        if word in f_7:
            ret += math.log2(2 + f_7[word] / 10)
    return ret


match_const = 1  # higher for better match, lower for fluency

import sys
while True:
    sys.stdout.write("上句: ");
    sys.stdout.flush()
    input = sys.stdin.readline()
    output = None
    mark = -1
    for round in range(1000):  # more rounds? not a good idea
        nw = []
        nw_mark = 0
        for i in range(len(input) - 1):
            nw_c, delta = match(input[i])
            nw.append(nw_c)
            # print(delta)
            nw_mark += delta * match_const
        nw = ''.join(nw)
        nw_mark += evaluate(nw)
        if nw_mark > mark:
            mark = nw_mark
            print("下句: ", mark)
            output = nw
    print("output:", output, "(", mark, ")")
    print()
