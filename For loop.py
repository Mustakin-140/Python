course = ["CSE141","CSE161","CSE181","CSE241","CSE265"]
print(course)
for x in course:
    #print(x)
    if x == "CSE181":
        continue
    print(x)

faculty = ["DMSS","SM","MMJR","AR","RAJ"]
for y in faculty:
    print(y)
    if y == "MMJR":
        break