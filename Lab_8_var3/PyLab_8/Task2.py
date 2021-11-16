import math
def func (b):
    return math.sqrt(4 * b + math.sin(math.sqrt (b**3)))
def integral(a,b) :
    return (b-a)*func(b)

x = float(input("Input X : "))
a = float(input("Input A : "))
b = float(input("Input B : "))

print("Result = {0:.2f}".format(integral(a,3)+integral(a,b)))