from cafe_coding_download import enable
from PIL import Image
import time

enable()

#for i in range(50):
#    print('■'*50)


# 文字色を黄色に
print('\033[38;2;200;190;0m',end='')
# 文字色を初期化して改行
print('\033[38;2;255;255;255m')


img = Image.open("D:\Image\original_qiitan.png")
rgb = img.convert('RGB')
size = rgb.size

while True:
    for x in range(size[0]):
        s = ''
        for y in range(size[1]):
            r,g,b = rgb.getpixel((y,x))

            # 文字色を変更
            print('\033[38;2;200;190;0m',end='')
            s += f'\033[38;2;{r};{g};{b}m■'
            print('\r' + s, end='')


            time.sleep(0.0001)

        print()

    for _ in range(51):
        print()
    print("\u001B[50A", end="")