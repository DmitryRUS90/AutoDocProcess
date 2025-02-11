import os

folder = os.getcwd()

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.pdf') and not file.startswith('~'):
            os.remove(os.path.join(root, file))
            print(os.path.join(root, file) + '  ------  УДАЛЕН')