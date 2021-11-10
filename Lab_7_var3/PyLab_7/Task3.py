(a,b,c) = ([],[],[])
sum = 0
n=int(input("Введіть n*n матриці : "))
for i in range(n) :
    a.append([float(input("Введіть значення елементу масива A {0} {1}: ".format(i+1,j+1))) for j in range(n)])
for i in range(n) :
    b.append([float(input("Введіть значення елементу масива B {0} {1}: ".format(i+1,j+1))) for j in range(n)]) 
for i in range(n) :
    c.append([float(a[i][j]+b[i][j]) for j in range(n)])
print(c) 