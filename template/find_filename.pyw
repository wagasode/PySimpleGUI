import PySimpleGUI as sg
from pathlib import Path
#--------------------vvv
#【1.使うライブラリをimport】

#【2.アプリに表示する文字列を設定】
title = "ファイル名を検索（フォルダ以下全ての）"
infolder = "."
label1, value1 = "検索文字", "test"

#【3.関数：　フォルダ内のファイル名に検索文字が含まれているかを調べる】
def findfilename(infolder, findword):
    cnt = 0
    msg = ""
    filelist = []
    for p in Path(infolder).rglob("*.*"):
        if p.name[0] != ".":
            filelist.append(str(p))
    for filename in sorted(filelist):
        if filename.count(findword) > 0:
            msg += f"{filename}\n"
            cnt += 1
    msg = f"ファイル数 = {str(cnt)}\n{msg}"
    return msg

#--------------------^^^
def execute():
    infolder= values["infolder"]
    value1 = values["input1"]
    #--------------------vvv
    #【4.関数を実行】
    msg = findfilename(infolder, value1)
    #--------------------^^^
    window["text1"].update(msg)
#アプリのレイアウト
layout = [[sg.Text("読み込みファイル", size=(14,1)),
           sg.Input(infolder, key="infolder"), sg.FolderBrowse("選択")],
          [sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
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
