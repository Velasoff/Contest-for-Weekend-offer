import json
from collections import OrderedDict

n = int(input())
data = []
for i in range(n):
    d = json.loads(input())
    for j in range(len(d['offers'])):
        data.append(dict(OrderedDict(sorted(d['offers'][j].items(), key=lambda t: t[0]))))

data = sorted(data, key=lambda x: x['price'])
d = json.dumps({'offers': data})
print(d)
