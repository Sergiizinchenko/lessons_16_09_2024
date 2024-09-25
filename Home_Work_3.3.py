new_lst = []
col_index = len(new_lst)
popolam_1 = int (colindex_1 / 2) #про
zal_dil= colindex_1 % 2  #залишок від ділення
if zal_dil == 0:
    new_list_1 = lst_1[:popolam_1]
    new_list_2 = lst_1[popolam_1:]
    print(popolam_1, [new_list_1, new_list_2])
else:
    new_list_1 = lst_1[:(popolam_1+1)]
    new_list_2 = lst_1[popolam_1+1:]
    print(popolam_1 ,[new_list_1,new_list_2])

