import functions
import PySimpleGUI as sg # "sg" represents "PySimpleGUI"
import time

sg.theme("DarkTeal11")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-do", key="todo") # hover the mouse over input line and will see a window with clue "Enter a To-do"; this is a "values"
add_button = sg.Button("Add") # add button; this is an "event"
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15)) # Title of the window
while True: #to keep the window open
    event, values = window.read(timeout=10) # .read - is a method. Displays the window on the screen
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S")) #call method fron cli.py file
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0] #[0] give us string
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo #this function will update a list with a new todo, replacing the existing todo
                functions.write_todos(todos) #then we right the updated list to the todos.txt
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 15))
        case "Complete": #"Complete"- is a label of a button in line 10;When the user press the button, that string is stored in variable "event"(line 18);if the match is "Complete", we want to delete the given item
            try:
                todo_to_complete = values['todos'][0] #when the user select one of todos, that dictionary is the values variable.[0]-> helps extract string with name of chosen todo
                todos = functions.get_todos() #now we want to remove chosen todo from list
                todos.remove(todo_to_complete)
                functions.write_todos(todos) #from functions.py file
                window['todos'].update(values=todos)
                window['todo'].update(value="")#to update input_box
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 15))
        case "Exit":
            break
        case 'todo':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close() #close - is a method. Close the window
