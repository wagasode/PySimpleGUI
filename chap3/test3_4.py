import PySimpleGUI as sg

def execute(value):
    msg = value + "さん、こんにちは。"
    window["text1"].update(msg)

title = "test4"
layout = [[sg.Text("あなたの名前は？"), sg.Input("お名前", key="input1")],
          [sg.Button("実行")],
          [sg.Text(key="text1")]]

window = sg.Window(title, layout)
while True:
    event, values = window.read()
    if event == None:
        break
    if event == "実行":
        execute(values["input1"])
window.close()
