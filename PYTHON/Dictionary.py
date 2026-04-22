#dictionary in python
info = {
    "name": "SumanNayak",
    "subject": ["python", "java", "C"],
    "topics": ("dict", "list", "tuple"),
    "age": 23,
    "is adult": True,
    "marks": 95.4,
    123.36 : 3563
}
print(info)
print(type(info))
print(len(info))
print(info["name"])
print(info["subject"])
info["name"] = "SUMAN"
info["surname"] = "NAYAK"
print(info)
#null dictionary
dict = {}
print(type(dict))
dict["Name"] = "Suman"
print(dict)
#Neasted Dictionary
student = {
    "name": "Suman",
    "marks":{
        "python": 95,
        "java": 90,
        "c": 85
    }
}