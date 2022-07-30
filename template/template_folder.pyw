import PySimpleGUI as sg
#--------------------vvv
#【1.使うライブラリをimport】

#【2.アプリに表示する文字列を設定】
title = "フォルダ選択のアプリ"
infolder = "."

#【3.関数】
def testfunc(path):
    msg = "フォルダ名 = " + path
    return msg
#--------------------^^^
def execute():
    infolder = values["infolder"]
    #--------------------vvv
    #【4.関数を実行】
    msg = testfunc(infolder)
    #--------------------^^^
    window["text1"].update(msg)
#アプリのレイアウト
layout = [[sg.Text("読み込みフォルダ", size=(14,1)),
           sg.Input(infolder, key="infolder"),sg.FolderBrowse("選択")],
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
