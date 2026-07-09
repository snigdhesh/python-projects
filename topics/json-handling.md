#### Reference: 
Check file handling concept on w3 schools

#### Overview
You can import default module from python called json. Everything in python is module, not library

    json.load("data.json") //Loads file
    json.loads("{'name':'naga','age':2}") //Prase json string to json object

More methods like `json.dumps()` on w3 schools

#### Examples:

##### Approach1
    with open("test.json","r") as file:
        data = json.load(file)
        print(data)

##### Approach2
    with open("test.json","r") as file:
        print(file.read())