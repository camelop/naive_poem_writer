from pace_statistic import *

position = []
for i in range(5):
    c_l = {}
    position.append(c_l)

for p in p_5_8:
    for line in p.content:
        for i in range(5):
            c = line[i]
            if c in position[i]:
                position[i][c] += 1
            else:
                position[i][c] = 1

usable = []
for i in range(5):
    u_l = []
    usable.append(u_l)

for i in range(5):
    for index, k_v in enumerate(sorted(position[i].items(), key=lambda k_v: k_v[1], reverse=True)):
        if index >= 500:
            break
        # print(k_v)
        usable[i].append(k_v[0])
    # print(usable[i])

import sys
import random
mark = ['，', '。\n', '，', '。\n']
for p in range(10):
    for i in range(4):
        for j in range(5):
            sys.stdout.write(usable[i][random.randint(0, len(usable[i]) - 1)])
        sys.stdout.write(mark[i])
    sys.stdout.write('\n')
