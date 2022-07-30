import PySimpleGUI as sg

def execute(value):
    msg = value + "さん、こんにちは。"
    window["text1"].update(msg)

title = "test5"
layout = [[sg.Text("あなたの名前は？"), sg.Input("お名前", key="input1")],
          [sg.Button("実行", size=(20,1), pad=(5,15))],
          [sg.Multiline(key="text1", size=(64,10))]]

window = sg.Window(title, layout, font=(None, 14))
while True:
    event, values = window.read()
    if event == None:
        break
    if event == "実行":
        execute(values["input1"])
window.close()
