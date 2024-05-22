# like as JSON
# list Mutable

myInfo = {
    "name": "Md Sakib Hasan",
    "age": 21,
    "isAdult": True,
    "favFood": ['rice', 'chiken']
}
print('My name is', myInfo["name"])
myInfo["surename"] = 'Halum'
print('after adding surename the dictionary is:', myInfo)

# nested dictionary
subjects = {
    "math": {
        '1st': 85,
        '2nd': 90
    }
}

print('Math 1st paper number', subjects["math"]["1st"])

print(subjects.keys())
