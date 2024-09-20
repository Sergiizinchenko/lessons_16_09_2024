from unicodedata import digit

user_input = input("Введіть 5-ти значне число:")
number = int(user_input)
digit_5 = number%10
digit_4 = (number//10)%10
digit_3 = (number//100)%10
digit_2 = (number//1000)%10
#digit_1 = number//10000
num= divmod(number,10000)

igit_1 = num[0]
print (digit_5,digit_4,digit_3,digit_2,digit_1,sep="")

#num = int(user_input)
#pal = 0
#while num != 0:
#    use = divmod(num, 10)
##    dig = use[1]
#   pal = pal*10+dig
#    num = use[0]

#print(pal)
