#Author: Elise Merrifield
#CIS 131
#M7 lab Shodan API for Python
#query shodan for "'in-tank inventory' state:'AZ'"


#install shodan
#import shodan and json
import json
import requests
import shodan

#add API key
api = shodan.Shodan('KWd68SjE7hekcNNoS92DtyV8AVLH70Jv')
query = "'in-tank inventory' state:'AZ'"

result = api.search(query)

# Shodan returns a dictionary of 'matches' and 'total'
matches = result["matches"]

# Matches is a json string so we convert it to json and then into a dictionary
inputdata = json.dumps(matches)
datadict = json.loads(inputdata)

# datadisct is a list of dictionary items, one item for earch result
for i in datadict:
	for key,value in i.items():
		print(i["data"])
