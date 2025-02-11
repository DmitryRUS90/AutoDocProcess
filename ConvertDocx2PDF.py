from docx2pdf import convert
import os

def word_convert(arr):
    out = []
    for file in arr:
        if '.docx' in file:
            out.append(file)

    return out

folder = os.getcwd()

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.docx') and not file.startswith('~'):
            #os.remove(os.path.join(root, file))
            convert(os.path.join(root, file))
            print(os.path.join(root, file) + '  ------  Преобразован в PDF')