import os
from borb.pdf import Document
from borb.pdf.pdf import PDF


def concatenate_two_docs(file1, file2):
    with open(file1, "rb") as pdf_file:
        print(file1, ' --- ЗАГРУЖАЕТСЯ')
        pdf1 = PDF.loads(pdf_file)

    with open(file2, "rb") as pdf_file:
        print(file2, ' --- ЗАГРУЖАЕТСЯ')
        pdf2 = PDF.loads(pdf_file)
    
    output_doc = Document()
    output_doc.add_document(pdf1)
    output_doc.add_document(pdf2)
    print(file2, "  ---------  ГОТОВ")
    with open(os.path.splitext(file2)[0] + "_union.pdf", "wb") as pdf_out:
        PDF.dumps(pdf_out, output_doc)    

paths_foto = []
paths_docs = []
folder_foto = os.getcwd() + '\Фото'
folder_docs = os.getcwd() + '\Материалы'

for root, dirs, files in os.walk(folder_foto):
    for file in files:
        if file.endswith('.pdf'):
            paths_foto.append(os.path.join(root, file))
            
for root, dirs, files in os.walk(folder_docs):
    for file in files:
        if file.endswith('.pdf'):
            paths_docs.append(os.path.join(root, file))
            print(paths_docs[-1])

if len(paths_foto) == len(paths_docs):
    for i in range(len(paths_docs)):
        concatenate_two_docs(paths_foto[i], paths_docs[i])
else:
    print("Количество фотографий и документов не совпадает. Проверьте исходные данные!")  