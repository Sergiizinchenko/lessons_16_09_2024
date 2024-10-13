def common_elements():
 my_list_one = list(range(0, 100, 3))
 my_list_wan = list(range(0, 100, 5))
 return set(el for el in my_list_one if el in my_list_wan)
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')



