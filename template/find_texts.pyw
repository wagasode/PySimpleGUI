import PySimpleGUI as sg
from pathlib import Path
#--------------------vvv
#【1.使うライブラリをimport】

#【2.アプリに表示する文字列を設定】
title = "テキストファイルを検索（フォルダ以下全ての）"
infolder = "."
label1, value1 = "検索文字列", "これは"
label2, value2 = "拡張子", "*.txt"

#【3.関数;　テキストファイルを検索する】
def findfile(readfile, findword):
    try:
        msg = ""
        p = Path(readfile)
        text = p.read_text(encoding="UTF-8")
        cnt = text.count(findword)
        if cnt > 0:
            msg = f"{readfile}:{str(cnt)}個見つかりました。\n"
        return msg
    except:
        return f"{readfile}:失敗しました。\n"

#【3.関数:　フォルダ以下全てのテキストファイルを検索する】
def findfiles(infolder, findword, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext):
        filelist.append(str(p))
    for filename in sorted(filelist):
        msg += findfile(filename, findword)
    return msg

#--------------------^^^
def execute():
    infolder = values["infolder"]
    value1 = values["input1"]
    value2 = values["input2"]
    #--------------------vvv
    #【4.関数を実行】
    msg = findfiles(infolder, value1, value2)
    #--------------------^^^
    window["text1"].update(msg)
#アプリのレイアウト
layout = [[sg.Text("読み込みフォルダ", size=(14,1)),
           sg.Input(infolder, key="infolder"),sg.FolderBrowse("選択")],
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
