import json
# json_data = ' {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5} '
# print(json.loads(json_data))
with open('awesome.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    # print(distro.keys())
    m = distro.get('_source').get('layers').get('data').get('data.data')
    print(m)