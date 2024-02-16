# найти самый большой простой делитель числа
# и простое и делитель


number1 = 600_851_475_143

class Numbers():
    
    def __init__(self, number):
        
        self.number = number
     
     
    # проверяет простое ли число    
    def is_simple(self, num):
        
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i == 0):
                return False
        return True
    
    
    #проверяет является ли число делителем
    def is_divide(self, num):
        
        if self.number % num == 0:
            return True
        else:
            return False
        
    #ищем наибольший общий делитель числа
    def find_bigges_simple_divide(self):
        
        while True:
            
            #перебираем эл.ты
            for el in range(self.number, 1, -1):
                
                #если эл.т  - простое число
                if self.is_simple(el):
                    
                    #если это число является делителем
                    if self.is_divide(el):
                        
                        return el
                    





test1 = Numbers(1355876)

print(test1.find_bigges_simple_divide())



        
        

