import functions
import PySimpleGUI as sg # "sg" represents "PySimpleGUI"

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-do", key="todo") # hover the mouse over input line and will see a window with clue "Enter a To-do"; this is a "values"
add_button = sg.Button("Add") # add button; this is an "event"
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15)) # Title of the window
while True: #to keep the window open
    event, values = window.read() # .read - is a method. Displays the window on the screen
    print(1, event) # "hello" appears, when you press some buttons, and then the window will be closed
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0] #[0] give us string
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo #this function will update a list with a new todo, replacing the existing todo
            functions.write_todos(todos) #then we right the updated list to the todos.txt
            window['todos'].update(values=todos)
        case 'todo':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close() #close - is a method. Close the window
