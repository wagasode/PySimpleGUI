import PySimpleGUI as sg

layout = [[sg.Text("1行目-1"), sg.Text("1行目-2")],
          [sg.Text("2行目-2"), sg.Input("2行目-2")],
          [sg.Button("3行目")]]

window = sg.Window("test2", layout)
while True:
    event, value = window.read()
    if event == None:
        break
window.close()
