import json
from pprint import pprint

filename = 'zseb.json'

json1_file = open(filename)
json1_str = json1_file.read()
json1_data = json.loads(json1_str)[0]
dic = json1_data
with open(filename) as json_data:
    data = json.load(json_data)
    #pprint(data)
'''
print(json1_file)
print(json1_str)
print(json1_data)
'''
#print(next(iter(json1_data.values())))
'''
for index in range(0,18):
	print(list(dic.keys())[index])
'''
key_1 = []
for key, value in dic.items():
	key_1.append(key)

for key, value in dic.items():
	if key == 'comments':
		print(value)
