while True:

    # Ваш код тут
    # if my_list.lower() != 'Yes':
    first_symbol = float(input("1st num:  "))
    my_operator = input("operator (+, -, /, *):  ")
    second_symbol = float(input("2nd num:  "))
    if my_operator not in ("+", "-", "*", "/"):
        result = "ERROR - wrong operator"
    if my_operator == "+":
        result = first_symbol + second_symbol
    elif my_operator == "-":
        result = first_symbol - second_symbol
    elif my_operator == "*":
        result = first_symbol * second_symbol
    elif my_operator == "/":
        if second_symbol != 0:
            result = first_symbol / second_symbol
        else:
            result = "ERROR - can't divide by zero"
    else:
        result = "ERROR - wrong operator"
    умова = input("Введіть 'так', щоб повернутися на початок програми: ")
    if умова.lower() != 'yes':
        break