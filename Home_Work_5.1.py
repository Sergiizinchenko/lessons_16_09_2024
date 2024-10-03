import keyword
import string
import sys
my_list = str(input("Введіть текст: "))
if my_list.count('_') >= 2 or my_list.count(' ') > 0 or my_list[0].isdigit():
    print("False")
    sys.exit()
if my_list.islower():
    print("лише малі літери")
    # if my_list[0].isalpha():
    if any(char in string.punctuation.replace('_', '') for char in my_list):
        print("False")
        # elif any(char in keyword.kwlist(' ', '') for char in my_list)
    elif my_list in keyword.kwlist:
        print("False")
    else:
        print("True")
    # else:
    # print("False")
elif my_list.isupper():
    print("Рядок містить лише великі літери.")
else:
    print("True")