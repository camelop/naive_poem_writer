import json
import pickle
import re
from poem import Poem

with open('raw_gsw.json', 'r') as f:
    data = json.load(f)
    '''
    data(dict)[KEY]: KEY in
    ['author', 'dynasty', 'name', 'poem']
    '''


# construct poem_list
poem_list = []
for d in data:
    poem_list.append(Poem(d))

with open('poem_list.data', 'wb') as f:
    pickle.dump(file=f, obj=poem_list)
