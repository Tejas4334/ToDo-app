import functions
import FreeSimpleGUI as Gui




label = Gui.Text("Type a TODO")
input_box = Gui.InputText(key ="todo", tooltip="Enter Todo")
add_button = Gui.Button("Add")
exit_button = Gui.Button("Exit")
edit_button = Gui.Button("Edit")
complete_button = Gui.Button("Complete")

todo_list = Gui.Listbox(values = functions.get_todo(),
                        key = "TodoList",
                        enable_events = True,
                        size = (45,10),
                        )

window = Gui.Window("To-Do List",
                    layout = [
                              [label],
                              [input_box,add_button],
                              [[edit_button,complete_button],todo_list],
                              [exit_button],
                              ],
                    font = ("Helvetica",12))

while True:
    event,values = window.read()
    print(event)
    print(values)

    match event:

        case "Add":

            todos = functions.get_todo()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            functions.Update_val(window,todos)

        case "Edit":
            todo_to_edit = values["TodoList"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.write_todos(todos)

            functions.Update_val(window,todos)

        case "Complete":
            Complete_todo = values["TodoList"][0]

            todos = functions.get_todo()
            todos.remove(Complete_todo)
            functions.write_todos(todos)

            functions.Update_val(window,todos)

        case "Exit" | Gui.WIN_CLOSED:
            break

window.close()

