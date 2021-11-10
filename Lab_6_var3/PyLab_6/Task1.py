"""
Дано n дійсних чисел : х1, х2, . . . хn
Знайти найбільше серед них
"""
# 0 Позначення
"""
Масив – list[float] - n
Координата елементу в масиві - int - i
Найбільше значення - float - bigger
"""
n = []
i = bigger = 0
while True :
    n.append((input("Введіть здачення числа : ".format(i))))
    if n[i] == "" :
        break
    n[i]=float(n[i])
    if n[i] > bigger:
        bigger = n[i]
    i+=1
print(bigger)

"""
- input - - - - - 
        Введіть здачення числа : 4
        Введіть здачення числа : 2
        Введіть здачення числа : 1
        Введіть здачення числа : 9
        Введіть здачення числа :

- output - - - - -
        9.0
"""