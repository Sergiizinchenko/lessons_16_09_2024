#first_list = [0, 1, 7, 2, 4, 8]
first_list =[1, 3, 5]
# first_list =[6]
#first_list = []
odd_list = []  # створення  нового пустого  списка
if first_list:
    end_element = first_list[-1]  # визначення значення останнього елемента
else:
    end_element = 0#отримуємо значення 0, якщо список пустий
for element in first_list:
    if first_list.index(element) % 2 == 0:
        odd_list.append(first_list[first_list.index(element)])
print(sum(odd_list) * end_element)





