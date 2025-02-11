from doc2docx import convert
import os

paths = []
folder = os.getcwd()
print(help(convert))

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.doc') and not file.startswith('~'):
            paths.append(os.path.join(root, file))
            convert(paths[-1])