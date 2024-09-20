
user_input = input("Введіть 4-х значне число:")
number = int(user_input)
digit_4 = number%10
digit_3 = (number//10)%10
digit_2 = (number//100)%10
digit_1 = number//1000
print (digit_1,digit_2,digit_3,digit_4,sep='\n')

