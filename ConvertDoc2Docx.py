from doc2docx import convert
import os

paths = []
folder = os.getcwd()

while True:
    key_press = input('Вы находитесь в каталоге: ' + folder + '. Продолжить? [y/n]')
    if key_press == 'y':
        break
    elif key_press == 'n':
        exit()

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.doc') and not file.startswith('~'):
            paths.append(os.path.join(root, file))
            convert(paths[-1])