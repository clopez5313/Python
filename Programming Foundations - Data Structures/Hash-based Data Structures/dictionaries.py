# Declare a dictionary.
dictionary = {"Name": "Zara","Age":7,"Class":"First"}

# Access the dictionary with its keys.
print("dictionary['Name']:", dictionary["Name"])
print("dictionary['Age']:", dictionary["Age"])

# Update an entry in the dictionary, and add new data.
dictionary["Age"] = 8
dictionary["School"] = "DPS School"

print("dictionary['Age']:", dictionary["Age"])
print("dictionary['School']:", dictionary["School"])

# Delete elements in the dictionary. The clear() method removes all entries in the dictionary.
del dictionary["Name"]
dictionary.clear()
del dictionary

# print("dictionary['Age']:", dictionary["Age"])
# print("dictionary['School']:", dictionary["School"])

# Accessing nested elements.
dictionary = {"Dictionary 1": {1: "Some"},
              "Dictionary 2": {"Name": "Text"}}
print(dictionary["Dictionary 1"])
print(dictionary["Dictionary 1"][1])
print(dictionary["Dictionary 2"]["Name"])
