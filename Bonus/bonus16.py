import PySimpleGUI as sg

label1 = sg.Text("Select file to compress:")
local1 = sg.Input() # for text box
chose_button1 = sg.FilesBrowse("Chose") # Special button, which already programmed to allows user select files

label2 = sg.Text("Select destination folder:")
local2 = sg.Input()
chose_button2 = sg.FolderBrowse("Chose") # Special button, which already programmed to

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, local1, chose_button1],
                           [label2, local2, chose_button2],
                           [compress_button]]) # File Compressor - name of the window
window.read()
window.close()