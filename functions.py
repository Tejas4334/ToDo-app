
def get_todo(filename = "files/todos.txt"):
    """this is to read the text into the file"""
    with open(f"{filename}",'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filename = "files/todos.txt" ):
    """this is to write the text into the file"""

    with open(f'{filename}', 'w') as file:
        file.writelines(todos_arg)

def Update_val(window, Data_stream, text_key ='todo', list_key ="TodoList"):
    """This function is used to clean and update the fields of Todo App"""

    window[text_key].update(value="")             # cleans the text_field
    window[list_key].update(values=Data_stream)   #updates the TodoList