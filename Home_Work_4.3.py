import random
# first_list = [1, 2, 3, 4, 5, 6, 7, 9]
#[1, 1, 2, 1] == [1, 2, 2]
#[6, 3, 7] == [6, 7, 3
my_list = []#створюємо список, який будемо наповнювати згідно умов задачі
my_list = [random.randint(1,100) for i in range(random.randint(3, 10))]
print(my_list)#друкуємо отриманмй список
number_el = len(my_list)-2#визначаємо другий з кінця елемент списку
#new_list = [element for element in my_list if my_list.index(element) == 0 or my_list.index(element)==2 or my_list.index(element) == number_el]
new_list = [element for element in my_list if my_list.index(element) in (0,2,number_el)]#додаємо в новий список елементи згідно умов задачі
print(new_list)
