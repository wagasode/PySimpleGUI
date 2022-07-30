import PySimpleGUI as sg
#--------------------
#【1.使うライブラリをimport】

#【2.アプリに表示する文字列を設定】
title = "入力欄が1つのアプリ"
label1, value1 = "入力欄1", "初期値1"

#【3.関数】
def testfunc(word1):
    return f"入力欄の文字列 ={word1}"

#--------------------
def execute():
    value1 = values["input1"]
    #--------------------
    #【4.関数を実行】
    msg = testfunc(value1)
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
