import PySimpleGUI as sg
import random
#--------------------
#【1.使うライブラリをimport】

#【2.アプリに表示する文字列を設定】
title = "入力した値を最大値とする乱数を出力するアプリ"
label1, value1 = "最大値", "10"

#【3.関数】
def dice(value1):
    max = int(value1)
    r = random.randint(1, max)
    return str(r)

#--------------------
def execute():
    value1 = values["input1"]
    #--------------------
    #【4.関数を実行】
    msg = dice(value1)
    #--------------------
    window["text1"].update(msg)

#アプリのレイアウト
layout = [[sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
          [sg.Button("実行", size=(20,1), pad=(5,15), bind_return_key=True)],
          [sg.Multiline(key="text1", size=(60,10))]]

#アプリの実行処理
window = sg.Window(title, layout, font=(None,14))
while True:
    event, values = window.read()
    if event == None:
        break
    if event == "実行":
        execute()
window.close()
