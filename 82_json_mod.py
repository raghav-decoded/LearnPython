'''
json = java script object notation

json.load(file_object)
    json.load() takes a file object and returns the json object.
    A JSON object contains data in the form of key/value pair.

json.loads() method
    can be used to parse a valid JSON string and convert it into a Python Dictionary.

json.dumps() function will convert a subset of Python objects into a json string. 
    sort_keys: 
        If sort_keys is True (default: False), then the output of dictionaries will be sorted by key.
'''
import json

data = '{"var1":"harry", "var2":56}'
# here data is a string
print(data)

parsed = json.loads(data)
# parsed is a dict
print(type(parsed))

#Task 1 - json.load?

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
# jscomp is js compatible
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
