import functions
import FreeSimpleGUI as Gui
import time
import os

if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt",'w') as file:
        pass

Gui.theme("Topanga")

clock = Gui.Text(key="clock")
label = Gui.Text("Type a TODO")
input_box = Gui.InputText(key ="todo", tooltip="Enter Todo",size=45)
add_button = Gui.Button("Add",size=8)
exit_button = Gui.Button("Exit",size=8)
edit_button = Gui.Button("Edit",size=8)
complete_button = Gui.Button("Complete",size=8)

prompt_msg = Gui.Text(key = "prompt")

todo_list = Gui.Listbox(values = functions.get_todo(),
                        key = "TodoList",
                        enable_events = True,
                        size = (45,10),
                        )

window = Gui.Window("To-Do List",
                    layout = [[clock],
                              [label],
                              [input_box,add_button],
                              [[edit_button,complete_button],todo_list],
                              [prompt_msg],
                              [exit_button],
                              ],
                    font = ("Helvetica",12))

while True:

    event,values = window.read(timeout=10)
    window['clock'].update(value = time.strftime("%d-%b-%Y , %H:%M:%S"))

    match event:

        case "Add":

            todos = functions.get_todo()
            new_todo = values['todo']+"\n"

            if new_todo == "\n":
                print("Make sure you enter the task to Add")
                Gui.popup("Make sure you enter the task to Add")

                continue

            todos.append(new_todo)
            functions.write_todos(todos)

            functions.Update_val(window,todos)

        case "Edit":
            try:
                todo_to_edit = values["TodoList"][0]
                new_todo = values["todo"] + "\n"

                if new_todo == "\n":
                    print("Make sure you enter the task to Edit with")
                    Gui.popup("Make sure you enter the task to Edit with")
                    continue



                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                functions.write_todos(todos)

                functions.Update_val(window,todos)

            except IndexError:
                print("Make sure you select a task to edit")
                Gui.popup("Make sure you select a task to edit")

        case "Complete":
            try:
                Complete_todo = values["TodoList"][0]

                todos = functions.get_todo()
                todos.remove(Complete_todo)
                functions.write_todos(todos)

                functions.Update_val(window,todos)

            except IndexError:
                print("Make sure you select a task to mark complete")
                Gui.popup("Make sure you select a task to mark complete")

        case "Exit" | Gui.WIN_CLOSED:
            break

window.close()

