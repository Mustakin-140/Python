#print("Welcome to\nPython")

print("Welcome to\npython")
#print("python")

name = "southeast university"
print(name + " is love")
print(type(name))
print(name.lower())
print(name.upper())
print(name.islower())
print(name.upper().isupper())
print(name.lower().islower())

dept= "Computer Science and Engineering"
print(len(dept))
print(len("bangladesh"))

city="chattogram"
print(city[6])
print(city.index("m"))
print(city.index("gram"))

course = "System Design"
print(course.replace("System","Database"))


#Slicing string
country = "Bangladesh"
print(country[3:7])

#slice from start
print(country[:5])

#slice to the end
print(country[5:])

#negative slicing
print(country[-5:-2])
