import math

def funct(x):
    return math.sqrt(4 * x + math.sin(math.sqrt (x**3) ))
def integral(a,b) :
    return (b-a)*funct(b)

x = float(input("Input X : "))
a = float(input("Input A : "))
b = float(input("Input B : "))

print("Result = {0:.2f}".format(integral(a,3)+integral(a,b)))