# JSON is commonly used with data APIs, especially from third parties. Here how we can parse JSON into a Python dictionary so it is easier to work with the data

import json

# sample JSON
userJSON  = '{"first_name": "John", "last_name": "Doe". "age": 30}'

# parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# turn dict into json
car = {"make": "Ford", "model": "Mustang", "year": 1960}
carJSON = json.dumps(car)
print(carJSON)