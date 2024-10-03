while True:
    first_symbol = float(input("1st num:  "))
    my_operator = input("operator (+, -, /, *):  ")
    second_symbol = float(input("2nd num:  "))
    result = None
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
    print(result)
    umova = input("Введіть 'yes', щоб повернутися на початок програми: ")
    if umova.lower() not in ("yes", "Y", "y", "ye"):
        break