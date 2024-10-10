my_str = str(input("Введіть число без коми:  "))
my_str_new = my_str
my_str = int(my_str)
if my_str <= 9:
    print(my_str)
else:
    # my_str = int(my_str)
    while my_str >= 10:
        # print(my_str)
        res = int(my_str_new[0])
        for ele in my_str_new[1:]:
            res *= int(ele)
            my_str = res
            my_str_new = str(res)
    print(res)