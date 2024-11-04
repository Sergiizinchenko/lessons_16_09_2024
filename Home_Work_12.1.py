import codecs
import re

def delete_html_tags(html_file, result_file='result.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        # with codecs.open("C:/Users/iuAD0COS/Lesson_16092024.py/draft.html", 'r', 'utf-8') as file:
        # text = file.read()
        # pattern = r"<.*?>"
        # pattern = r"<*?/>"
        #
        result = re.sub(r"<.*?>", '', html, flags=re.DOTALL)
        with open(result_file, 'w') as f:
            # with open(result.txt, 'w') as f:
            f.write(result)
            return result
            # print(result.txt)
            # return result.txt


delete_html_tags('draft.html', 'result.txt')


