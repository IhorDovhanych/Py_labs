'''
Дано текстовий файл, який містить дійсні числа.
Яких елементів більше – додатних чи від’ємних.
'''
with open("PyLab_19/numbers.txt") as file:
    plus_num = minus_num = count = 0
    for i in file:
         count += 1
    file.seek(0)
    for i in range(count):
        line = file.readline()
        nums = map(lambda el:int(el), line.split(sep=' ') )
        for el in nums:
            if el >= 0:
                plus_num += 1
            else:
                minus_num += 1
    if plus_num > minus_num:
        print("Додатніх елементів більше")
    elif plus_num < minus_num:
        print("Від'ємних елементів більше")
    else:
        print("Кількість додатніх і від'ємних дорівнюють один одному")
            
            