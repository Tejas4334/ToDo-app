import functions
import FreeSimpleGUI as gui

label = gui.Text("Type a TODO")
input_box = gui.InputText(key = "todo", tooltip="Enter Todo")
add_button = gui.Button("Add")
exit_button = gui.Button("Exit")
edit_button = gui.Button("Edit")

window = gui.Window("To-Do List",
                    layout = [
                              [label],
                              [input_box,add_button],
                              [edit_button,exit_button],
                              ],
                    font = ("Helvetica",12))

while True:
    event,values = window.read()
    # print(event)
    # print(values)

    match event:
        case "Add":

            todos = functions.get_todo()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)


        case "Edit":
            pass
        case "Complete":
            pass
        case "Exit" | gui.WIN_CLOSED:
            break

window.close()

