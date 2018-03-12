import json
from pprint import pprint
import open_jason as oj

#Open zseb.txt with function written in
#open_jason.py file
dic_list = oj.zseb()

#In that file we can find a list of dics
element_list = []
for elements in dic_list:
	element_list.append(elements)

#pprint(key_1)

'''
for key, value in element_list[0].items():
	if key == 'comments':
		for k, v in value.items():
			if k == 'data':
				for k3, v3 in v[0].items():
					if k3 == 'owner':
						for k4, v4 in v3.items():
							pprint(v4)
'''

#Here we check all the first level keys and their number in the dataset
#lot = len(element_list)

#count = {}
'''
for index in range(lot):
	for key, value in element_list[index].items():
		if key in count:
			count[key] += 1
		else:
			count[key] = 1
'''
#pprint(count)
'''
This is how you get the name of your commenters and how many times
they have commented

'''
commenter_count = {}
for index_0 in range(len(element_list)):
    for k, v in element_list[index_0].items():
    	if k == 'comments':
    		for k1, v1 in v.items():
    			if k1 == 'data': 
    			#pprint(len(v))
    				for index in range(len(v1)):
    					for k2, v2 in v1[index].items():
    						if k2 == 'owner':
    							for k3, v3 in v2.items():
    								if k3 == 'username':
    									if v3 in commenter_count:
    										commenter_count[v3] += 1
    									else:
    										commenter_count[v3] = 1
#pprint(commenter_count)

for commenter in sorted(commenter_count, key=commenter_count.get, reverse = True):
	print(commenter, commenter_count[commenter])
'''
	if key == 'comments':
		for k, v in value.items():
			if k == 'data':
				for k3, v3 in v[0].items():
					if k3 == 'owner':
						for k4, v4 in v3.items():
							pprint(v4)
							'''