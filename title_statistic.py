import pickle
from poem import Poem

with open('poem_list.data', 'rb') as f:
    poem_list = pickle.load(f)

title_s = {}
for p in poem_list:
    title_nw = p.title
    if title_nw in title_s:
        title_s[title_nw].append(p)
    else:
        title_s[title_nw] = [p]

for index, k_v in enumerate(sorted(title_s.items(), key=lambda f: len(f[1]), reverse=True)):
    if index > 100:
        break
    print("Title: ", k_v[0], "\t# ", len(k_v[1]))

for i in range(100, 105):
    print(title_s['浣溪沙'][i])
