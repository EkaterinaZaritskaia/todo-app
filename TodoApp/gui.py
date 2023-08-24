import functions
import PySimpleGUI as sg # "sg" represents "PySimpleGUI"

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-do") # hover the mouse over input line and will see a window with clue "Enter a To-do"
add_button = sg.Button("Add") # add button

window = sg.Window('My To-Do App', layout=[[label, [input_box, add_button]]]) # Title of the window
window.read() # .read - is a method. Displays the window on the screen
# print("hello") -> "hello" appears, when you press some buttons, and then the window will be closed
window.close() # .close - is a method. Close the window
