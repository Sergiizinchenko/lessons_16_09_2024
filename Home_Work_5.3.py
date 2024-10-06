import string
my_list = str(input("Введіть текст: "))
my_list = my_list.title()#все з великої літери
remove_chars = set(
    string.punctuation + ' ')  # У цьому коді ми створюємо множину remove_chars, яка містить всі знаки пунктуації та пробіли.
# Використовуємо генератор списку для фільтрації символів
cleaned_text = ''.join(char for char in my_list if char not in remove_chars)
print(f'#{cleaned_text[:140]}')





