import PySimpleGUI as sg

label1 = sg.Text("Enter Feet:")
local1 = sg.Input()

label2 = sg.Text("Enter Inches:")
local2 = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label1, local1],
                                        [label2, local2],
                                        [button]])

window.read()
window.close()