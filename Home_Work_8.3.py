def find_unique_value(some_list):
    from collections import Counter
    counter = Counter(some_list)
    result = [(element, count) for element, count in counter.items()]
    min_count = float('inf')
    for element, count in result:
        if count < min_count:
            min_count = count
            min_element = element
    return min_element
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

