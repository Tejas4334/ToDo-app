
def get_todo(filename = "todos.txt"):
    """this is to read the text into the file"""
    with open(f"{filename}",'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filename = "todos.txt" ):
    """this is to write the text into the file"""

    with open(f'{filename}', 'w') as file:
        file.writelines(todos_arg)

