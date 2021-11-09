import random
"""
Дана цілочислова матриця 
Розмістити елементи парних стовпців у порядку зростання.
"""
a = []
sum = []
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n) :
    a.append([random.randint(0,10) for j in range(m)]) 
print("Ісходна матриця : \n {0} \n".format(a))
l = m
for j in range(m) :
    while l < m :
        if (j+1)%2==0 :  
                sum.append(a[i][j])
                i+=1
        if i == n :
            i = 0
            break
        l+=1
    sum.sort()
    for i in range(n) :
        if (j+1)%2==0 :
            a[i].insert(j,sum[i])
            a[i].pop(j+1)
    sum.clear()
    l=i=0
print("Посортирована матриця : \n {0}".format(a))


