""" Визначити добуток від’ємних елементів матриці з обома непарними індексами. """
A = []
sum = 0
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n) :
    A.append([float(input("Введіть значення елементу масива {0}{1}: ".format(i+1,j+1))) for j in range(m)])
    for j in range(m) :
        if not (j+1)%2==0 :
            if A[i][j] < 0 :
                sum += A[i][j]
print(sum)
