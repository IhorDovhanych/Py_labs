def func(x) :
    sum = 0
    if x < 0 :
        for i in range(1,6) :
            sum += x**i
        return sum
    else :
        for i in range(1,6) :
            sum += x**i
        return sum
    
a = float(input("Введіть значення А : "))
b = float(input("Введіть значення В : "))

print("u = {0}".format(func(a)+func(2)+func(b)))