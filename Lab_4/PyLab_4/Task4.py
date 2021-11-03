import math
"""
y=cos(x**2+log(x,10)) x**2+log(x,10)>0
y=1/x**2+log(x,10) x**2+log(x,10)<0
y=cos(x) x**2+log(x,10)=0
"""
# 0.Позначення
"""
Функція - float - y
Змінна - float - x
"""
x=float(input("Введіть значення змінної : "))
y=x**2 + math.log(x,10)
if y > 0 :
    print(math.cos(y))
elif y < 0 :
    print(1/y)
else :
    print(math.cos(x))

"""
- input - - - - - 
                    x = 5
- output - - - - -
                    0.8439300570712257
"""

