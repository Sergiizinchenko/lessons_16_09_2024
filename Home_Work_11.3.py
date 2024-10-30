def is_even(number):
    # for num in range(0,8,2 ):

    if int(str(number)[-1]) in range(0, 8, 2):
        print(int(str(number)[-1]))

        return True

    return False


# gen = is_even(2494563894038**2)

# assert is_even(2494563894038**2) == True, 'Test1'

# assert is_even(1056897**2) == False, 'Test2'

assert is_even(24945638940387 ** 3) == False, 'Test3'


