import json

#writing json
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "ML"]
}
with open("jsonData.json", "w") as file:
    json.dump(data, file)

#reading json
with open("jsonData.json", "r") as file:
    print(json.load(file))

# Convert JSON string → Python object
json_str = '{"name" : "Bob", "age" : 23}'
data1 = json.loads(json_str)
print(data1["name"])

#Convert Python object → JSON string

data = {"x": 10, "y": 20}
json_str = json.dumps(data)

print(json_str)