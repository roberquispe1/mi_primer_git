import json
with open ("json_ejemplo.json")as data:
    json_file = data.read()
json_python = json.loads(json_file)
print (json_python)

