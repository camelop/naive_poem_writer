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


def match(x):
    if x in before:
        return sorted(before[x].items(),
                      key=lambda k_v: k_v[1],
                      reverse=True)[0][0]
    else:
        return "好"


for p in p_5_8:
    nw = None
    for line in p.content:
        if nw is None:
            nw = line
        else:
            for i in range(5):
                create_pair(nw[i], line[i])
            nw = None

import sys
while True:
    sys.stdout.write("input: ");
    sys.stdout.flush()
    input = sys.stdin.readline()
    output = []
    for i in range(len(input) - 1):
        output.append(match(input[i]))
    print("output:", ''.join(output))
