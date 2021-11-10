import math
"""
Перевірити справедливість рівності при заданій точності epsilon
ln|sin(x)|=-ln2-cos2x-(cos(4x)/2n)-...-(cos(2xn)/n)-..., 0 < x < pi
"""
x = float(input("Введіть значення x, x є (0,pi) : "))
if not 0 < x < math.pi :
    print("Хибне значення")
eps = float(input("Введіть значення epsilon : "))
ln_sin = math.log((abs(math.sin(x))), 10)
n = 1
s = -math.log(2, 10)-math.cos(2*x)-(math.cos(4*x)/(2*n))
m = 0
while True :
    if s < eps :
        if ln_sin==s :
            print("Рівність справедлива")
            break
        else :
            print("Рівність несправедлива")
            break
    n += 1
    m += math.cos(2*x*n)/n
    s -= m
