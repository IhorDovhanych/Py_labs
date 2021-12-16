class Stuff:
    
    def __init__(self, name, bithday, work_accept_day, salary):
        self.name = name 
        # ^ example: Довганич ДІО ^
        self.bithday = list(map(lambda el:int(el), bithday.split(sep=".")))
        # ^ example: 01.02.2004 ^
        self.work_accept_day = list(map(lambda el:int(el), work_accept_day.split(sep=".")))
        # ^ example: 01.02.2004 ^
        self.salary = salary
        # ^ example: 3000 ^
        
    def WorkStage(self, actual_date):
        actual_date = list(map(lambda el:int(el), actual_date.split(sep=".")))
        
        output = (actual_date[2]-self.work_accept_day[2])*365
        output += (actual_date[1]-self.work_accept_day[1])*30
        output += actual_date[0]-self.work_accept_day[0]
        
        if output == 0:
            return "Started work today/Never worked"
        elif output == 1:
            return output
        elif output > 1:    
            return output
        else:
            return Exception("Fail data")
        
    def Age(self,actual_date):
        actual_date = list(map(lambda el:int(el), actual_date.split(sep=".")))
        
        output = (actual_date[2]-self.bithday[2])*365
        output += (actual_date[1]-self.bithday[1])*30
        output += actual_date[0]-self.bithday[0]
        
        output //= 365
        
        if output == 0:
            return "Just both"
        elif output == 1:
            return output
        elif output > 1:    
            return output
        else:
            return Exception("Fail data")
    def SumSalary(self, actual_date):
        return (self.WorkStage(actual_date)//30)*self.salary
        
    
Ivan = Stuff("Іван НІТ","01.02.2004","12.10.2020",3000)
Kristina = Stuff("Крістіна БКБ","01.12.2005","03.11.2020",3500)

print("Стаж роботи {0} : {1} дн.".format(Ivan.name, Ivan.WorkStage("02.12.2020")))
print("Стаж роботи {0} : {1} дн.".format(Kristina.name, Kristina.WorkStage("02.12.2020")))
print("\n")
print("Вік {0} : {1} р.".format(Ivan.name,Ivan.Age("01.01.2021")))
print("Вік {0} : {1} р.".format(Kristina.name,Kristina.Age("01.01.2021")))
print("\n")
print("Зарплата {0} : {1} грн".format(Ivan.name,Ivan.SumSalary("02.12.2020")))
print("Зарплата {0} : {1} грн".format(Kristina.name,Kristina.SumSalary("02.12.2020")))
        
        
        