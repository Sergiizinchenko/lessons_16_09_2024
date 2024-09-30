first_list = [0,1,0,12,3]
#first_list = [0]
#first_list = [1, 0, 13, 0, 0, 0, 5]
#first_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
i = 0
j = 0
kil_nuliv = first_list.count(0)#кількість нулів у списку
while i < kil_nuliv:
    first_list.remove(0)  # проходимо по списку і видаляємо 0 зі списку
    # print(first_list)
    i += 1
while j < kil_nuliv:
    first_list.append(0)  # добавляємо  кількість 0 що було в кінець списку
    #     print (first_list)
    j += 1
print(first_list)





