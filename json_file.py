# Json is  commonly used with API(application program interface), we learn hw to parse Json into a python dictionary

import json

# sample Json
detailJSON = '{"first_name": "Fortunes", "last_name": "onyekwere", "age": 21}'

#parse to dictionary
detail = json.loads(detailJSON)

print(detail)
print(detail['first_name'])

# Getting back to json from a dictionary

carDict = {'make': 'toyota', 'model': 'camry', 'year': 2014}

carJSON = json.dumps(carDict)
print(carJSON)      