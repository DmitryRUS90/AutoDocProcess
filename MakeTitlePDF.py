import pikepdf
import os

def del_pages(pdf, arr, num_pages=16):
    max = arr[1]
    min = arr[0] - 1
    del pdf.pages[max:num_pages]
    del pdf.pages[0:min]
    
    return pdf

def doc_crushing(doc_path, arr, outpdf):
    with pikepdf.open(doc_path) as pdf:
        # Смотрим сколько страниц в pdf
        num_pages = len(pdf.pages)
        # Удаляем страницы из pdf
        del_pages(pdf, arr, num_pages)
        pdf.save(root + '\\' + outpdf)


paths = []
folder = os.getcwd()
start_page = 1
finish_page = 1

while True:
    key_press = input('Вы находитесь в каталоге: ' + folder + '. Продолжить? [y/n]')
    if key_press == 'y':
        break
    elif key_press == 'n':
        exit()

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.pdf'):
            paths.append(os.path.join(root, file))
            file_for_print = file + '_for_print!.pdf'
            path_print_file = os.path.join(root, file_for_print)
            doc_crushing(paths[-1], [start_page,finish_page], file_for_print)
            print(file_for_print, '  СОЗДАН')
            


