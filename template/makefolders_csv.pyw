import PySimpleGUI as sg
from pathlib import Path
import csv
#--------------------vvv
#【1.使うライブラリをimport】

#【2.アプリに表示する文字列を設定】
title = "名簿のCSVファイルでフォルダを作成"
infile = "namelist.csv"
label1, value1 = "書き出しフォルダ", "outputfolder"

#【3.関数】
def makefolders(readfile, savefolder):
    msg = ""
    Path(savefolder).mkdir(exist_ok=True)
    f = Path(infile).open(encoding="UTF-8")
    csvdata = csv.reader(f)
    for row in csvdata:
        for foldername in row:
            newfolder = Path(savefolder).joinpath(foldername)
            newfolder.mkdir(exist_ok=True)
            msg += f"{savefolder}に{foldername}を作成しました。\n"
    return msg
#--------------------^^^
def execute():
    infile = values["infile"]
    value1 = values["input1"]
    #--------------------vvv
    #【4.関数を実行】
    msg = makefolders(infile, value1)
    #--------------------^^^
    window["text1"].update(msg)
#アプリのレイアウト
layout = [[sg.Text("読み込みファイル", size=(14,1)),
           sg.Input(infile, key="infile"), sg.FileBrowse("選択")],
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
