import PySimpleGUI as sg
#--------------------vvv
#【1.使うライブラリをimport】

#【2.アプリに表示する文字列を設定】
title = "ファイル選択+入力欄2つのアプリ"
infile = "test.txt"
label1, value1 = "入力欄1", "初期値1"
label2, value2 = "入力欄2", "初期値2"

#【3.関数】
def testfunc(path, word1, word2):
    msg = "ファイル名 = " + path + "\n"
    msg += "入力欄の文字列 = " + word1 + word2
    return msg
#--------------------^^^
def execute():
    infile = values["infile"]
    value1 = values["input1"]
    value2 = values["input2"]
    #--------------------vvv
    #【4.関数を実行】
    msg = testfunc(infile, value1, value2)
    #--------------------^^^
    window["text1"].update(msg)
#アプリのレイアウト
layout = [[sg.Text("読み込みファイル", size=(14,1)),
           sg.Input(infile, key="infile"), sg.FileBrowse("選択")],
          [sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
          [sg.Text(label2, size=(14,1)), sg.Input(value2, key="input2")],
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