import json
from pprint import pprint

def zseb():
	filename = 'zseb.json'
	json1_file = open(filename)
	json1_str = json1_file.read()
	json1_data = []
	for item in range(len(json.loads(json1_str))):
		json1_data.append(json.loads(json1_str)[item])
	dic_list = json1_data
	return dic_list

