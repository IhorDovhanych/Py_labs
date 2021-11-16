""" Побудувати квадратну матрицю А, елементи якої задаються формулою: """
def sum(a) :
    sum_1 = 0  
    for i in range(a+1) :
        sum_1 +=((-1)**a)**a
    return sum_1
a = []
j_n = 1
n=int(input("Введіть розмірність матриці : "))
for i in range(n) :
    a.append([(i+j+2 if (i+1)*(1+j)<3 else sum(j)) for j in range(n)])
print(*a, sep="\n")

