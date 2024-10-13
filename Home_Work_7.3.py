def second_index(text, some_str):
    if 2 == len(some_str):
        i = text.find(some_str[1])
        new_text = text[:i] + text[i + 1:]
        result = new_text.index(some_str[1])
    elif 2 == len(text):
        result = None
    else:
        i = text.index(str(some_str))
        new_text = text[:i] + text[i + 1:]
        result = new_text.index(some_str) + 1
    return result
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')