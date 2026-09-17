
# Dictionaries  - stores data as key : value pair

data={
    "name" : "Deva",
    "age" : 20,
    "city" : "Coimbatore",
    "course" : "Computer Science",
    "CGPA" : 8.4,
    "status" : "Completed"
}

print(data["name"])   # lookup - access data based on their key
print(data.get("name"))  # similar to data access above but its safe to use 'get' because it doesn't through an error when element is not found it shows 'None' msg

print(data.keys())
print(data.values())

for key, value in data.items():   # items method return key and value output
    print(key, value)


data.update({"year":2026})  # its like upsert where a data is updated if present or else inserted if not present
print(data)

data.pop("year")
print(data)


data2={
    "name" : "Anu",
    "age" : 20,
    "city" : "Erode",
    "subjects" : ["Tamil","Computer","English","Maths"],
    "CGPA" : 8.4,
    "status" : "Completed"
}

for k,v in data2.items():
    print(k,":",v)

#to access a subject from that list

print(data2["subjects"][2])

for subject in data2["subjects"]:
    print(subject)