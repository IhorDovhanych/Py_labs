import random
"""
Дана цілочислова матриця 
Розмістити елементи парних стовпців у порядку зростання.
"""
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
a = [[random.randint(-10, 10) for j in range(m)] for i in range(n)]
print("Ісходна матриця : \n {0} \n".format(a))

for j in range(1,m,2):
    for i in range(n):
        for k in range(n):
            if a[i][j] > a[k][j]:
                c = a[k][j]
                a[k].insert(j,a[i][j])
                a[i].insert(j,c)
                a[i].pop(j+1)
                a[k].pop(j+1)
print("Посортирована матриця : \n {0}".format(a))



