import string
# def remove_punctuation(input_string):
#    translator = str.maketrans('', '', string.punctuation)
#    return input_string.translate(translator)
#
# text = "Привіт, світ! Як справи?"
# clean_text = remove_punctuation(text)
# print(clean_text)  # Виведе: Привіт світ Як справи
my_list = str(input("Введіть текст: "))
my_list1 = my_list.title()
remove_chars = set(
    string.punctuation + ' ')  # У цьому коді ми створюємо множину remove_chars, яка містить всі знаки пунктуації та пробіли.
# Використовуємо генератор списку для фільтрації символів
cleaned_text = ''.join(char for char in my_list1 if char not in remove_chars)
print(f'#{cleaned_text[:140]}')





