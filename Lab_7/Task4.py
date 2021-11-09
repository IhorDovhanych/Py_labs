a = []
sum = []
n=int(input("Введіть кількість рядків матриці : "))
m=int(input("Введіть кількість стовбців матриці : "))
for i in range(n) :
    a.append([float(input("Введіть значення елементу масива {0} {1}: ".format(i+1,j+1))) for j in range(m)]) 
b = list(a)
for i in range(n) :
    for j in range(m) : 
            if (j+1)%2==0 :  
                sum.append(a[i][j])
                sum.sort()
    a[i][j]=sum[i]
                
print(sum)        
print(a)