import matplotlib.pyplot as plt
import pandas as pd
import docx
import re
from collections import Counter

lion = docx.Document('lion.docx') #берем произведение
text = [] #бустой лист для того, чтобы добавить в него текст
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
            'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
            'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#все элементы, которые могут входить в слова или даты
for paragraph in lion.paragraphs:
         for run in paragraph.runs:
                 # получение текста абзаца
                p_text = p.text
print(p_text)
runs_txt = []
for run in p.runs:
    runs_txt.append(run.text)
print(''.join(runs_txt))


import re
words = re.findall(r'\w+', open('file.txt').read().lower())
counts = Counter(words).most_common(10)
print(counts)