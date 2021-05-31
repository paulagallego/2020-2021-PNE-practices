import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINTA = '/info/species'
ENDPOINTB = '/info/assembly'

PARAMETERSA = '?content-type=application/json'
PARAMETERSB = '?content-type=application/json'


connection = http.client.HTTPConnection(SERVER) #ensembl database connection
connection.request('GET', ENDPOINTA + PARAMETERSA)
response = connection.getresponse()

response_dict = json.loads(response.read().decode()) #obtain dict
complete_list_species = response_dict['species']
name_species = []
for elem in complete_list_species:
    name_species.append(elem['display_name'])

print(complete_list_species)