''' DICTIONARIES
    unordered (no sequence is required - data or entries have no order)
    mutable 
    indexed 
    No duplication of data (each key is unique)

    {key1:value1, key2:value2 ...}

    copy()
        Used to create a copy of a dict
        = creates a ptr
    dict[key] = value 
        to add another element
    update({key:value})
    del dict[key]
    keys()
        returns the keys
    items()
        returns the items
'''

# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
# d2["Ankit"] = "Junk Food"
# d2[420] = "Kebabs"
# print(d2)
# del d2[420]
# print(d2["Shubham"])
# d3 = d2.copy()
# del d3["Harry"]
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(d2.items())
