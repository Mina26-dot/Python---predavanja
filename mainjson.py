import json
from textwrap import indent

with open("data/user.json", 'r') as file:
    data = json.load(file)
    data.append({
        "name": "Marko",
        "age": 43
    })
print(data)


with open("data/user.json", 'w') as file:
    json.dump(data, file, indent=4)
