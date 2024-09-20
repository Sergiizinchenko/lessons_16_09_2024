from unicodedata import digit
user_input = input("Введіть 5-ти значне число:")
number = int(user_input)
digit_1 = divmod(number,10000)
digit_2 = divmod(digit_1[1],1000)
digit_3 = divmod(digit_2[1],100)
digit_4 = divmod(digit_3[1],10)
#digit_5 = divmod(digit_4[1],1)
print (digit_4[1],digit_4[0],digit_3[0],digit_2[0],digit_1[0],sep="")

