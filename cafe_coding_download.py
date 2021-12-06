import time
import random
from ctypes import windll, wintypes, byref
from functools import reduce

def enable():
  INVALID_HANDLE_VALUE = -1
  STD_INPUT_HANDLE = -10
  STD_OUTPUT_HANDLE = -11
  STD_ERROR_HANDLE = -12
  ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
  ENABLE_LVB_GRID_WORLDWIDE = 0x0010

  hOut = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
  if hOut == INVALID_HANDLE_VALUE:
    return False
  dwMode = wintypes.DWORD()
  if windll.kernel32.GetConsoleMode(hOut, byref(dwMode)) == 0:
    return False
  dwMode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
  if windll.kernel32.SetConsoleMode(hOut, dwMode) == 0:
    return False
  return True

def r():
    return random.random()

def r_g():
    return random.gammavariate(1,2)

def main():
    while True:
        l_word = ['hoge-2021','fuga-4.4','piyo-9.3.0','sore_ppoi_yatu','gettwo-6.4.3']
        word = l_word[int(r() * 5)]
        print('Downloading {}'.format(word))
        time.sleep(0.5)

        r_n = r() * 100
        if r_n < 10:
            print('Requirement already satisfied: {} in C:\\Program Files\\Soreppoi\\Path\\packages'.format(word))
            print()
            time.sleep(0.5)
            continue

        elif r_n < 20:
            # 文字色を黄色に
            print('\033[38;2;200;190;0m',end='')
            print('You are trying to install old version, however new version is available.')
            print('It is recommended that you install the newer version.')
            # 文字色を初期化して改行
            print('\033[38;2;255;255;255m')
            time.sleep(0.5)
            continue

        elif r_n < 30:
            # 文字色を赤に
            print('\033[38;2;255;0;0m',end='')
            print('ERROR: Could not install packages due to an EnvironmentError: ', end='')
            print('[WinError 5] アクセスが拒否されました。: C:\\Program Files\\Soreppoi\\Path')
            print('Consider using the `--user` option or check the permissions.')
            # 文字色を初期化して改行
            print('\033[38;2;255;255;255m')
            time.sleep(0.5)
            continue

        download_num = int(2 + r() * 6)
        for j in range(download_num):
            for i in range(51):
                percentage = min(round(i * 2 + r(),1), 100)
                # 文字幅調整
                if percentage == 100:
                    percentage = ' 100'
                print('\r[{}] {}%'.format('#' * i + '-' * (50 - i), percentage), end='')

                if r() * 100 < 3:
                    time.sleep(r_g() * 0.1)
                else:
                    time.sleep(r() * 0.02)
            print()

        print('Installing collected packages: {}'.format(word))
        time.sleep(0.5)
        print('  Setup {} in progress'.format(word), end='')
        time.sleep(0.1 * r_g())
        print('(\r  Setup {} in progress .'.format(word), end='')
        time.sleep(0.5 * r_g())
        print('(\r  Setup {} in progress ..'.format(word), end='')
        time.sleep(0.5 * r_g())
        print('(\r  Setup {} in progress ...'.format(word), end='')
        time.sleep(0.5 * r_g())
        print('(\r  Setup {} in progress ... done'.format(word))
        time.sleep(0.5)
        print('Successfully installed {}'.format(word))
        time.sleep(0.5)
        print()


if __name__ == "__main__":
    enable()
    main()