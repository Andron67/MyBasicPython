#Урок 1.13. Обработка ошибок. Исключения 

import math #Математическая библиотека

#Обработка последовательности чисел с возможными ошибками ввода

#Простейшая обработка без учёта ошибок
def process_data(inputs):
    for my_input in inputs:
        my_num = int(my_input)
        print(my_num*3, end = ' ')

#Используется проверка ввода
def process_data2(inputs):
    for my_input in inputs:
        if my_input.isdigit():      #Если состоит из чисел
            my_num = int(my_input)  #Преобразуем 
            print(my_num*3, end = ' ')
        else: 
            print("Не число", end = ' ')
            
#Используется обработка исключений
def process_data3(inputs):
    for my_input in inputs:
        try:
            my_num = int(my_input)
            print(my_num*3, end = ' ')
        except:
            print("Не число", end = ' ')
            
#Используется обработка исключений
def process_data4(inputs):
    for my_input in inputs:
        try:
            my_num = int(my_input)
            my_num2 = 1/math.sqrt(my_num) # 1 делить на корень(sqrt) из числа
            print(my_num2)
        except Exception as e:
            print(str(e))

#Точка входа в программу
def main():
    numbers = ['2', '3', '15', '7', '11', '16']
    process_data(numbers)
    print("")

    numbers2 = ['2', '3', '15', 'Hello', '11', '16']
    process_data2(numbers2)
    print("")
    
    process_data3(numbers2)
    print("")
    print("")
    
    process_data4(numbers2)
    print("")
    
    numbers3 = ['2', '3', 'Hello', '-11', '16', '7', '0', '22']
    process_data4(numbers3)
    
    return 0

if __name__ == '__main__':
	main()
    
#--------------------------------------------------
#try: 
#    print("Привет")
#except:
#    print("Произошла ошибка")
#else: 
#    print("Ошибки не произошло")


#try:
#   f = open("demofile.txt")  #Открываем файл
#   f = write("Привет")       #Пишем в него "Привет"
#except: 
#   print("Ошибка при записи в файл")  #Произошла ошибка записи в файл
#finally:  #Закрываем файл независимо от того произошла ошибка или нет
#   f.close()                        


