import re
import docx

def calc_num(string, value):
    split_str = string.split('.')
    split_str[-1] = str(int(split_str[-1]) + value)
    return '.'.join(split_str)


doc = docx.Document('! Практикум итог (2).docx')

pattern = r'[Р|р]ис\.\xa04\.\d+'
value = -126

all_paras = doc.paragraphs
for paras in all_paras:
    f = re.findall(pattern, paras.text)
    for i in f:
        if i:
            replace = calc_num(i, value)
            paras.text = re.sub(i, replace, paras.text)

doc.save('Практикум итог.docx')           

