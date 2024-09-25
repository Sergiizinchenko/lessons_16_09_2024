user_input = input("Введіть вираз (використовуйте крапку у десятковому числі ):")
number = list(user_input)
element_1 = '+'
element_2 = '-'
element_3 = '*'
element_4 = '/'

if element_1 in number:
        ele= number.index(element_1)#визначаємо індекс знаку у списку
        ele_2 = int(ele+1)#індекс для визначення  другої частини списку
        num_1 = float(''.join(number[:ele]))#отримуємо перше число з початку списку до знаку
        num_2 = float(''.join(number[ele_2:]))#отримуємо друге число від знака і до кінця списку
        print(num_1+num_2)
if element_2 in number:
        ele= number.index(element_2)
        ele_2 = int(ele+1)
        num_1 = float(''.join(number[:ele]))
        num_2 = float(''.join(number[ele_2:]))
        print( num_1 - num_2)
if element_3 in number:
        ele= number.index(element_3)
        ele_2 = int(ele+1)
        num_1 = float(''.join(number[:ele]))
        num_2 = float(''.join(number[ele_2:]))
        print( num_1*num_2)
if element_4 in number:
        ele= number.index(element_4)
        ele_2 = ele+1
        num_1 = float(''.join(number[:ele]))
        num_2 = float(''.join(number[ele_2:]))
        if num_2 == 0:#
            print("Помилка, на 0 ділити не можна")
        else:
            print( num_1/num_2)