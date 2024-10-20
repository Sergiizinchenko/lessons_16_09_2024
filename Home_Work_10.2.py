def first_word(text):
    """ Пошук першого слова """

    # text = str(text)

    word = ""

    start_col = False

    for char in text:

        if char not in [' ', ',', '.']:
            start_col = True

        if start_col:

            if char in [' ', ',', '.']:
                break

            word += char

    return word


# for char in text:

#      if char in [' ', ',', '.']:

#         break

#      word += char

# print(word)

assert first_word("Hello world") == "Hello", 'Test1'

assert first_word("greetings, friends") == "greetings", 'Test2'

assert first_word("don't touch it") == "don't", 'Test3'

assert first_word(".., and so on ...") == "and", 'Test4'

assert first_word("hi") == "hi", 'Test5'

assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')