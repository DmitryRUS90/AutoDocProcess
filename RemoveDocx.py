import os

folder = os.getcwd()

while True:
    key_press = input('Вы находитесь в каталоге: ' + folder + '. Продолжить? [y/n]')
    if key_press == 'y':
        break
    elif key_press == 'n':
        exit()

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.docx') and not file.startswith('~'):
            os.remove(os.path.join(root, file))
            print(os.path.join(root, file) + '  ------  УДАЛЕН')