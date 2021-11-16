import random
"""
Дана цілочислова матриця 
Розмістити елементи парних стовпців у порядку зростання.
"""
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
a = [[random.randint(-10, 10) for j in range(m)] for i in range(n)]
print("Ісходна матриця : \n ")
print(*a, sep="\n")

for j in range(1,m,2):
    for i in range(n):
        for k in range(n):
            if a[i][j] > a[k][j]:
                a[k][j], a[i][j] = a[i][j],a[k][j]
                
print("Посортирована матриця : \n")
print(*a, sep="\n")



