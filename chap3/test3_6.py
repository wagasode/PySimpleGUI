import PySimpleGUI as sg

title = "ファイル選択テスト"
layout = [[sg.Text("ファイル選択", size=(12,1)),
           sg.Input(".", key="infile"),
           sg.FileBrowse("選択")]]

window = sg.Window(title, layout, font=(None, 14))
while True:
    event, values = window.read()
    if event == None:
        break
window.close()
