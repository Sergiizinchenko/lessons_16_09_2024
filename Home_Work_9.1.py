def popular_words(text, words):
    from collections import Counter

    counter = dict(Counter(text.lower().split()).most_common())

    return {key: counter.get(key, 0) for key in words}


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')



