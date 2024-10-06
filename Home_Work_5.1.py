import keyword
import string
import sys
my_list = str(input("Введіть текст: "))
if my_list.count('__')>=1 or my_list.count(' ') >0 or my_list[0].isdigit()  :
    print(False)
    sys.exit()
if any(char for char in my_list if char.isupper()):
    print (False)
    sys.exit()
if any(char in string.punctuation.replace('_', '') for char in my_list):
    print(False)
elif my_list in keyword.kwlist:
    print(False)
else:
    print(True)

