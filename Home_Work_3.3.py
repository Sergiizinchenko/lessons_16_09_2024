lst_1 = [1,3,4,5,6,7]
colindex_1 = len (lst_1)
popolam_1 = colindex_1 / 2
a  = popolam_1 % 2
if a == 0:
    new_list_1 = lst_1[:popolam_1]
    new_list_2 = lst_1[popolam_1:]
    print (popolam_1,new_list_1,new_list_2)
else:
    print(a,popolam_1)
#print (lst_1)