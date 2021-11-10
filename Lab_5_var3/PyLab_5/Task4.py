"""
Нехай X0=X1=1 Xi=Xi-1+Xi-2, де і=2,3... Визначити Xn
"""

x_0 = x_1 = 1
i = int(input("Введіть значення i : "))
if i < 2 :
    print("Хибне значення")
elif i == 2 :
    x_n = x_1 + x_0
    print(x_n)
else :
    x_a = 1
    x_b = 2
    for j in range(2,i) :
        x_c = x_b
        x_b += x_a
        x_a = x_c
    print(x_b)



"""
- input - - - - - 
        Введіть значення i : 9

- output - - - - -
        55
"""
