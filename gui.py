# import modules.functions
import FreeSimpleGUI as gui

label = gui.Text("Type a TODO")
input_box = gui.InputText()
add_button = gui.Button("ADD")


window = gui.Window("To-Do List", layout = [[label],
                                                [input_box],
                                                [add_button]
                                                ])
window.read()

window.close()

