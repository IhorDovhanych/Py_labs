class Matrix:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.matrix=[]
    #==============={getter and setter for x value
    @property
    def x (self):
        return self.__x
    @x.setter
    def x (self,value):
        self.__x = value
    #===============} {getter and setter for y value
    @property
    def y (self):
        return self.__y
    @y.setter
    def y (self,value):
        self.__y = value
    #===============} { some methoids
    def matrix_el_input(self):
        for i in range(self.__y):
            self.matrix.append([])
            for j in range(self.__x):
                self.matrix[i].append(float(input("el {0} {1} = ".format(j+1, i+1))))
    def max_el(self):
        argument = self.matrix[0][0]
        for i in range(self.__y):
            for j in range(self.__x):
                if self.matrix[i][j] > argument:
                    argument = self.matrix[i][j]
        return argument
            
    def min_el(self):
        argument = self.matrix[0][0]
        for i in range(self.__y):
            for j in range(self.__x):
                if self.matrix[i][j] < argument:
                    argument = self.matrix[i][j]
        return argument
    
    def __str__(self):
        return str(self.matrix)


m1 = Matrix(2,7)

print(m1.x, m1.y)
m1.x = 4
print(m1.x, m1.y)

m1.matrix_el_input()
print("Мінімальне значення : {0}".format(m1.min_el()))
print("Максимальне значення: {0}".format(m1.max_el()))
print(m1)
    