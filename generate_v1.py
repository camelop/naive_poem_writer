from pace_statistic import *

character_list = {}
for p in p_5_8:
    for line in p.content:
        for c in line:
            if c in character_list:
                character_list[c] += 1
            else:
                character_list[c] = 1

usable = []

for index, k_v in enumerate(sorted(character_list.items(), key=lambda k_v: k_v[1], reverse=True)):
    if index >= 500:
        break
    # print(k_v)
    usable.append(k_v[0])

import sys
import random
mark = ['，', '。\n', '，', '。\n']
for p in range(20):
    for i in range(4):
        for j in range(5):
            sys.stdout.write(usable[random.randint(0, len(usable) - 1)])
        sys.stdout.write(mark[i])
    sys.stdout.write('\n')
