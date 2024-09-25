#lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 2, 3]
lst = [1, 2, 3, 4, 5]
#lst = [1]
#lst = []

col_index = len(lst) #кількість елементів у списку
popolam_1 = int (col_index / 2) #визначаємо на скільки ділемо список
zal_dil= col_index % 2  #визначаємо залишок від ділення
if zal_dil == 0:   # якщо залишок 0 то кількість елементів парна
    new_list_1 = lst [:popolam_1]
    new_list_2 = lst [popolam_1:]
    print(popolam_1, [new_list_1, new_list_2])
else: #кількість елементів не парна
    new_list_1 = lst [:(popolam_1+1)]
    new_list_2 = lst [popolam_1+1:]
    print(popolam_1 ,[new_list_1,new_list_2])

