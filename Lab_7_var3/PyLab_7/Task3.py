c = []
n=int(input("Введіть n*n матриці : "))

for i in range(n) :
    c.append([0])
    for j in range(n) :
        a = float(input("Введіть значення елементу масива A {0} {1}: ".format(i+1,j+1)))
        b = float(input("Введіть значення елементу масива B {0} {1}: ".format(i+1,j+1))) 
        c[i].append(a+b)
    c[i].pop(0)
print(c) 