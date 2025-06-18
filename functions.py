
def get_todo(filename = "files/todos.txt"):
    with open(f"{filename}",'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filename = "files/todos.txt" ):
    with open(f'{filename}', 'w') as file:
        file.writelines(todos_arg)