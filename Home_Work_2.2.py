user_input = input("Введіть 5-ти значне число:")
number = int(user_input)
digit_5 = number%10
digit_4 = (number//10)%10
digit_3 = (number//100)%10
digit_2 = (number//1000)%10
digit_1 = number//10000
print (digit_5,digit_4,digit_3,digit_2,digit_1,sep="")