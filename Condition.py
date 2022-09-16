"""
conditions (6):
Equal: a == b
Not equal: a != b
Greater then: a > b
Less than: a < b
Greater or equal: a >= b
Less or equal: a <= b
"""
a = 10
b = 10
if b > a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")
else:
    print("a is greater than b")


c = 200
d = 33
e = 500
if(e > c) and (e > d):
    print("e is the greatest")

m = 200
n = 33
p = 500
if(p > m) or (p < n):
    print("p is the greatest")