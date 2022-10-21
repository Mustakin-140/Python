x = lambda a: a+10
print(x(10))

y = lambda b,c : b * c
print(y(5,6))

z = lambda  p,q,r : p + q + r
print(z(5,55,7))


def myfunc(n):
    return  lambda  a : a*n
mydouble = myfunc(2)
mytriple = myfunc(3)
print(mydouble(11))
print(mytriple(11))