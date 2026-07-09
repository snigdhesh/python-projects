import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print("Y: ", y)
print("X: ", x)
print("y.name: ", y["name"])


with open("test.json","r") as file:
    data = json.load(file)
    print(data)

with open("test.json","r") as file:
    print(file.read())