import random
""" 
Дана цілочислова прямокутна матриця.
Визначити номер рядка, в якому знаходиться найдовша серія однакових елементів.
"""
(a,b,sum,l,j,y) = ([],[],[],0,0,1)
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовбців матриці : "))
a = [[random.randint(0, 1) for j in range(m)] for i in range(n)]
for i in range(n) :
    while l < m :  
        sum.append(a[i][j])
        j+=1
        l+=1
    print(sum)
    x=0.1
    for el in sum :
        if x == el :
            y+=1
        x = el
    b.append(y)
    j=l=0
    y=1
    sum.clear()
print("{0} - рядок має найдовшу серію повторення елементів".format(b.index(max(b))+1))
    
        