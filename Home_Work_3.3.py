lst_1 = [1,2,3]
colindex_1 = len(lst_1)
popolam_1 = int (colindex_1 / 2)
zal_dil= colindex_1 % 2  #залишок від ділення
if zal_dil == 0:
    new_list_1 = lst_1[:popolam_1]
    new_list_2 = lst_1[popolam_1:]
    print(popolam_1, [new_list_1, new_list_2])
else:
    new_list_1 = lst_1[:popolam_1]
    new_list_2 = lst_1[popolam_1:]
    print([new_list_1,new_list_2])
#print (lst_1)
