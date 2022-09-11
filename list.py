course = ["Fundamental","C Programming","Discrete Mathematics","Data Structures","Algorithm"]
print(course)
print(course[1])
print(len(course))
print(type(course))

if "Algorithm" in course:
    print("Yes")

course[4] = "Java"
print(course)

course.insert(5,"Algorithm")
print(course)

course.append("Numerical Methods")
print(course)

course.insert(6,"Microproccesor")
print(course)

Departmemt = ["CSE","EEE","BBA"]
course.extend(Departmemt)
print(course)

initial = ("DMSS","SM","GZI","MMJR","AR","RAJ")
course.extend(initial)
print(course)

course.remove("BBA")
print(course)

course.sort()
print(course)

course.sort(reverse=True)
print(course)

course.reverse()
print(course)

subject = course.copy()
print(subject)

initial1 = ["DMSS","SM","GZI","MMJR","AR","RAJ"]
initial2 = ["AHQ","SAMD","SBB","MDSR","MSRS"]
initial3 = initial1 + initial2
print(initial3)