# -*- coding: utf-8 -*-
import os

with open('File_path.txt', 'w', encoding='utf-8') as f:
    p = os.getcwd()
    for filename in os.listdir(p):
        s = os.path.abspath(filename) + '\n'
        f.write(s)