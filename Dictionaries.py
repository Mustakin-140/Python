course = {
    "title": "Database Design",
    "code": "CSE383",
    "faculty": "MMJR",
    "Grade": "A",
    "Grade": "A-",
    "Credit": 3

}
#print dictionary
print(course)
#print value of the key
print(course["title"])
#length of the dictionary
print(len(course))
#type of the dictionary
print(type(course))
#access an item
x = course["code"]
print(x)
#another way
y = course.get("code")
print(y)

#add new item
z = course.keys()
print(z)
course["room"] = "google meet"
print(z)
print(course)


#update item
course.update({"comment":"Good"})
print(course)

#remove item
course.pop("comment")
print(course)
"""
#empty dictionary
course.clear()
print(course)
"""

#copy dictionary
mydict = course.copy()
print(mydict)