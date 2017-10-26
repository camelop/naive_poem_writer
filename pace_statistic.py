import pickle
from poem import Poem

with open('poem_list.data', 'rb') as f:
    poem_list = pickle.load(f)

pace_s = {}
for p in poem_list:
    pace_nw = str(p.pace())
    if pace_nw in pace_s:
        pace_s[pace_nw].append(p)
    else:
        pace_s[pace_nw] = [p]

for index, pace in enumerate(sorted(pace_s.items(), key=lambda f: len(f[1]), reverse=True)):
    if index > 4:
        break
    # print("Pace: ", pace[0], "\t# ", len(pace[1]))


p_5_8 = pace_s[str((5, 5, 5, 5, 5, 5, 5, 5))]

f_5_8 = {}
c_5_8 = {}
for p in p_5_8:
    for line in p.content:
        for i in range(4):
            word = line[i] + line[i + 1]
            if word in f_5_8:
                f_5_8[word] += 1
            else:
                f_5_8[word] = 1
        for c in line:
            if c in c_5_8:
                c_5_8[c] += 1
            else:
                c_5_8[c] = 1

p_7 = pace_s[str((7, 7, 7, 7))] + pace_s[str((7, 7, 7, 7, 7, 7, 7, 7))]

f_7 = {}
c_7 = {}
for p in p_7:
    for line in p.content:
        for i in range(6):
            word = line[i] + line[i + 1]
            if word in f_7:
                f_7[word] += 1
            else:
                f_7[word] = 1
        for c in line:
            if c in c_7:
                c_7[c] += 1
            else:
                c_7[c] = 1
'''
for i in range(1000, 1005):
    print(p_5_8[i])
'''
