def is_palindrome(text):

 import string

 text_1= (text.translate(str.maketrans('', '', (string.punctuation)+' '))).upper()

 text_2 = text_1[::-1]

 if text_1==text_2:

    return True

 else:

    return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'

assert is_palindrome('0P') == False, 'Test2'

assert is_palindrome('a.') == True, 'Test3'

assert is_palindrome('aurora') == False, 'Test4'

print("ОК")