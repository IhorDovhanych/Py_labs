with open("PyLab_19/numbers.txt") as file:
    A = []
    plus_num = minus_num = count = 0
    for i in file:
         count += 1
    file.seek(0)
    for i in range(count):
        line = file.readline()
        nums = map(lambda el:int(el), line.split(sep=' ') )
        for el in nums:
            if el >= 0:
                A.append(el)
    A.append(sum(A))
    print(A)