"""
Дано дійсне число: а
З’ясувати, чи належать це число інтервалу (3;7)U[8;9)U(11;22.4)
"""
# 0.Позначення
"""
Число а - float - a
"""
a=float(input("Введіть значення числа а : "))
if 3<a<7 or 8<=a<9 or 11<a<22.4 :
    print("Число належить проміжку (3;7)U[8;9)U(11;22.4)")
else :
    print("Число неналежить проміжку (3;7)U[8;9)U(11;22.4)")


"""
- input - - - - - 
                    5
- output - - - - -
                    Число належить проміжку (3;7)U[8;9)U(11;22.4)
"""