import win32api
import os
import time

paths = []
folder = os.getcwd()

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('print!.pdf') and file.startswith('Л'):
            print(file, ' ------------  ', root)
            win32api.ShellExecute(2, "print", file, None, root, 0)
            time.sleep(10)