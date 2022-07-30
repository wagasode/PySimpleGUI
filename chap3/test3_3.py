import PySimpleGUI as sg

def execute():
    msg = "ボタンが押されました。"
    window["text1"].update(msg)

title = "test3"
layout = [[sg.Text("こんにちは。", key="text1")],
          [sg.Button("実行")]]

window = sg.Window(title, layout)
while True:
    event, value = window.read()
    if event == None:
        break
    if event == "実行":
        execute()
window.close()
