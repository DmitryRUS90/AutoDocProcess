import img2pdf
import os

size = [img2pdf.in_to_pt(8.3), img2pdf.in_to_pt(11.7)]
layout_function = img2pdf.get_layout_fun(size)

paths = []
folder = os.getcwd() + '\Фото'

while True:
    key_press = input('Вы находитесь в каталоге: ' + folder + '. Продолжить? [y/n]')
    if key_press == 'y':
        break
    elif key_press == 'n':
        exit()

files = os.listdir(folder)
for file in files:
    if file.endswith('.jpg') or file.endswith('.jpeg'):
        print(file)
        pdf = img2pdf.convert(folder + '\\' + file, layout_fun = layout_function)
        with open(folder + '\\' + os.path.splitext(file)[0] + '.pdf', 'wb') as f:
            f.write(pdf)  