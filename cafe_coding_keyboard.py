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

        print('\r' + s, end='')

        if data[i] == '\n':
            s = ''
            #改行後の空白は一気に表示
            while data[i+1] == ' ':
                s += data[i+1]
                i+=1
            print('\r' + s, end='')

        i+=1

    # すべて文字を表示しきったら初期化
    if i == len(data):
        i = 0
        s = ''
        print()
        print()





