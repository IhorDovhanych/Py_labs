"""
Дано число n є N
Побудувати алгоритм для визначення кількості одиниць  у записі цього числа n
"""
#0 Позначення
"""
Число - int - n
Кількість одиниць - int - k
"""
n = int(input("Введіть натуральне число n : "))
k = 0
for i in range(len(str(n))) :
    if n%10 == 1 :
        k += 1
    n //= 10
print(k)

"""
- input - - - - - 
        Введіть натуральне число n : 121

- output - - - - -
        2
"""