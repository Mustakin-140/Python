'''
def my_function():
    print("Hello")
my_function()

def name(fname):
    print(fname + " Rahman")
name("Ashiqur")
name("Mijanur")


def my_func(fname,lname):
    print(fname + " " + lname)
my_func("Mijanur", "Rahman" )


def func(*kids):
    print("The youngest child is" + kids[2])
func("Emil","Tobias")

def country(country = "Bangladesh"):
    print("I am from "+ country)
country("Italy")
country("England")
country()
country("Australia")
'''

def value(x):
    return  5 * x
print(value(3))
print(value(5))
print(value(9))