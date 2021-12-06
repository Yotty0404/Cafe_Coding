import time
import random
from ctypes import windll, wintypes, byref
from functools import reduce

def r():
    return random.random()

def r_g():
    return random.gammavariate(1,2)


'''

リビルドを開始しました...
1>------ すべてのリビルド開始: プロジェクト:FugaClass, 構成: Debug Any CPU ------
1>D:\PG\新しいフォルダー\FugaClass\Class1.cs(20,13,20,16): warning CS0162: 到達できないコードが検出されました
1>D:\PG\新しいフォルダー\FugaClass\Class1.cs(14,13,14,18): warning CS0414: フィールド 'Class1.value' が割り当てられていますが、値は使用されていません
1>  FugaClass -> D:\PG\新しいフォルダー\FugaClass\bin\Debug\FugaClass.dll
2>------ すべてのリビルド開始: プロジェクト:HogeHogeApp, 構成: Debug Any CPU ------
2>D:\PG\新しいフォルダー\HogeHogeApp\Form1.cs(13,6,13,10): warning CS0658: 'test' は認識できる属性の場所ではありません。この宣言の属性の場所として使用できるのは 'type' です。このブロック内の属性はすべて無視されます。
2>D:\PG\新しいフォルダー\HogeHogeApp\Form1.cs(28,37,28,39): warning CS1998: この非同期メソッドには 'await' 演算子がないため、同期的に実行されます。'await' 演算子を使用して非ブロッキング API 呼び出しを待機するか、'await Task.Run(...)' を使用してバックグラウンドのスレッドに対して CPU 主体の処理を実行することを検討してください。
2>D:\PG\新しいフォルダー\HogeHogeApp\Form1.cs(29,43,29,45): warning CS1998: この非同期メソッドには 'await' 演算子がないため、同期的に実行されます。'await' 演算子を使用して非ブロッキング API 呼び出しを待機するか、'await Task.Run(...)' を使用してバックグラウンドのスレッドに対して CPU 主体の処理を実行することを検討してください。
2>  HogeHogeApp -> D:\PG\新しいフォルダー\HogeHogeApp\bin\Debug\HogeHogeApp.exe

1>------ ビルド開始: プロジェクト: Genetic_Algorithm, 構成: Debug Any CPU ------
========== すべてリビルド: 2 正常終了、0 失敗、0 スキップ ==========

'''
project_num = 0
project_no = 0
project_name = ''
file_name = ''
ext = ''

sol_start = 'ビルドを開始しました...'
sol_end = '========== すべてビルド: {} 正常終了、0 失敗、0 スキップ =========='
pro_start = '{}>------ ビルド開始: プロジェクト: {}, 構成: Debug Any CPU ------'
pro_end = '{}>  {} -> C:\PG\{}\\bin\Debug\{}.{}'

warning0 = '{}>C:\PG\{}\{}\{}.cs({},13,{},16): warning CS0162: 到達できないコードが検出されました'
warning1 = "{}>C:\PG\{}\{}\{}.cs({},13,{},18): warning CS0414: フィールド 'Class1.value' が割り当てられていますが、値は使用されていません"
warning2 = "{}>C:\PG\{}\{}\{}.cs({},6,{},10): warning CS0658: 'test' は認識できる属性の場所ではありません。この宣言の属性の場所として使用できるのは 'type' です。このブロック内の属性はすべて無視されます。"
warning3 = "{}>C:\PG\{}\{}\{}.cs({},6,{},8): warning CS1998: この非同期メソッドには 'await' 演算子がないため、同期的に実行されます。'await' 演算子を使用して非ブロッキング API 呼び出しを待機するか、'await Task.Run(...)' を使用してバックグラウンドのスレッドに対して CPU 主体の処理を実行することを検討してください。"
l_warning = [warning0, warning1, warning2, warning3]

while True:
    l_word = ['HogehogeApp','FugaApp','PiyoClass','MyClass','CalcClass']

    project_num = 2 + int(r()*7)

    print(sol_start)

    for project_no in range(1, project_num+1):
        project_name = l_word[int(r()*5)]
        file_name = 'Form1.cs' if 'App' in project_name else 'Class1.cs'
        ext = 'exe' if 'App' in project_name else 'dll'

        print(pro_start.format(project_no, project_name))

        r_n = r() * 100
        if r_n < 40:
            time.sleep(r() * 0.1)
        elif r_n < 80:
            time.sleep(r_g() * 0.5)
        else:
            time.sleep(r_g() * 1)

        # 警告の数
        warning_num = int(r()*8)
        l_warning_num = [int(r()*4) for _ in range(warning_num)]
        # エラーコード順に並び替える
        l_warning_num.sort()

        gyou_no = 0
        temp_warning_num = -1
        for w_num in l_warning_num:
            if temp_warning_num != w_num:
                temp_warning_num = w_num
                gyou_no = 10 + int(r() * 200)

            else:
                gyou_no += int(r() * 200)
            print(l_warning[w_num].format(project_no, project_name, project_name, file_name, gyou_no, gyou_no))
            time.sleep(0.01)

        time.sleep(0.01)
        print(pro_end.format(project_no, project_name, project_name, project_name, ext))

    time.sleep(0.5)
    print(sol_end.format(project_num))
    print()
    print()

    time.sleep(1)