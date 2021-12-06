import keyboard
import time
import random
from ctypes import windll, wintypes, byref
from functools import reduce

from cafe_coding_download import enable

enable()

f = open('cafe_coding_download.py', 'r', encoding='UTF-8')

data = f.read()
f.close()
i = 0
s = ''

while True:
    if keyboard.read_key():
        s += data[i]
        print(s)
        print("\u001B[1A", end="")

        if data[i] == '\n':
            s = ''

        i+=1

    # すべて文字を表示しきったら初期化
    if i == len(data):
        i = 0
        s = ''
        print()
        print()





