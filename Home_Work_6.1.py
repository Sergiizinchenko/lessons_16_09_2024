import string
my_str = str(input("Введіть текст:  "))
a = my_str[0]
b = my_str[2]

index_a = string.ascii_letters.find(a)
index_b = string.ascii_letters.find(b) + 1
my_str1 = string.ascii_letters[index_a:index_b]

print(my_str1)


