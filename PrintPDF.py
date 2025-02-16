import win32api
import os
import time

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
        if file.endswith('print!.pdf'):
            print(file, ' ------------  ', root)
            win32api.ShellExecute(2, "print", file, None, root, 0)
            time.sleep(10)