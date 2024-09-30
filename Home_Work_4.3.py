import random

#

# first_list = [1, 2, 3, 4, 5, 6, 7, 9]

#[1, 1, 2, 1] == [1, 2, 2]

#[6, 3, 7] == [6, 7, 3

my_list = []

my_list = [random.randint(1,100) for i in range(random.randint(3, 10))]

print(my_list)

number_el = len(my_list)-2

#new_list = [element for element in my_list if my_list.index(element) == 0 or my_list.index(element)==2 or my_list.index(element) == number_el]

new_list = [element for element in my_list if my_list.index(element) in (0,2,number_el)]

#new_list.append(first_list[0],first_list[2])

#,first_list[2],first_list(number_of_el-2))

print(new_list)

#if my_list.index(element) in (0, 2, 5):