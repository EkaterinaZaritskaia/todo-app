import functions
import PySimpleGUI as sg # "sg" represents "PySimpleGUI"

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-do", key="todo") # hover the mouse over input line and will see a window with clue "Enter a To-do"; this is a "values"
add_button = sg.Button("Add") # add button; this is an "event"

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15)) # Title of the window
while True: #to keep the window open
    event, values = window.read() # .read - is a method. Displays the window on the screen
    print(event) # "hello" appears, when you press some buttons, and then the window will be closed
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close() #close - is a method. Close the window
