def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Всё работает правильно.

#1.Функция с параметрами по умолчанию:
print_params(0, 2, 3)                             #0 2 3                            
print_params(0, 2)                                #0 2 True                         
print_params(0)                                   #0 строка True                    
print_params()                                    #1 строка True                    
print_params(b=25)                                #1 25 True                        
print_params(c=[0, 2, 3])                         #1 строка [0, 2, 3]               
print_params(*[0, 2, 3])                          #0 2 3                            
                                                  
#2.Распаковка параметров:                         
values_list = [1, 'abc', 1 == 1]                  
values_dict = {'a': 1.0, 'b': 59, 'c': 'qaz'}     
print_params(*values_list)                        #1 abc True
print_params(**values_dict)                       #1.0 59 qaz

#3.Распаковка + отдельные параметры:
values_list_2 = [1+1j, 'sdf']
print_params(*values_list_2, 42)                  #(1+1j) sdf 42
