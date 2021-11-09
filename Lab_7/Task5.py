import random
""" 
Дана цілочислова прямокутна матриця. Визначити кількість стовпців, 
які містять хоча б один нульовий елемент.
"""
(a,k) = ([],0)
n=int(input("Введіть розмірність матриці матриці n*n : "))
for i in range(n) :
    a.append([random.randint(0,5) for j in range(n)]) 
print("Матриця : \n {0} \n".format(a))
for j in range(n) :
    for i in range(n) :
        if a[i][j] == 0 :
            k+=1
            break
print(f"{k} - кількіть стовпців що містять хоча б 1 нульвий елемент")     
    