def second_index(text, some_str):
  if len(some_str) >=2:
      ele = some_str
      i: int = text.index(ele)
      new_text = (text[:i]+text[i+1:])
  while:
        i: int = text.index(some_str)
         new_text = (text[:i] + text[i + 1:])
  return new_text.index(ele)
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')