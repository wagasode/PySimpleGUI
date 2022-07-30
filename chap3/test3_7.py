import PySimpleGUI as sg

title = "フォルダ選択テスト"
layout = [[sg.Text("フォルダ選択", size=(12,1)),
           sg.Input(".", key="infolder"),
           sg.FolderBrowse("選択")]]

window = sg.Window(title, layout, font=(None, 14))
while True:
    event, values = window.read()
    if event == None:
        break
window.close()
