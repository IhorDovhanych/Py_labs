import random
""" 
Дана цілочислова прямокутна матриця.
Визначити номер рядка, в якому знаходиться найдовша серія однакових елементів.
"""
(j,y,q,r) = (0,1,0,0)
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовбців матриці : "))
a = [[random.randint(0, 1) for j in range(m)] for i in range(n)]
print(*a, sep="\n")
for i in range(n) :
    x=0.1
    for el in a[i] :
        if x == el :
            y+=1
        x = el
        if y > q:
            q = y
            r = i
    j=0
    y=1
print("{0} - рядок має найдовшу серію повторення елементів".format(r+1))
    
        