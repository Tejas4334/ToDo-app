from functions import get_todo,write_todos
import time
now = time.strftime("%d-%b-%Y , %H:%M")
User_prompt = "Enter Todo : "
# todos = []
print("It is :- ",now)
while True:
    user_action = input("Enter Action (add,show,edit,complete,exit) : ")
    user_action = user_action.strip()

    if (user_action.startswith("Add")) | (user_action.startswith("add")):
        todos = get_todo()

        todos.append(f"{user_action[4:]}. \n")

        write_todos(todos)

    elif (user_action.startswith("Show")) | (user_action.startswith("show")):
        print(f"The task list is ")

        todos = get_todo()

        for index,item in enumerate(todos):
            print(f"{index + 1}-> {item}",end="")

    elif (user_action.startswith("Edit")) | (user_action.startswith("edit")):
        try:
            num = int(user_action[5:])

            todos = get_todo()

            print(f"Selected Task is \n{todos[num-1]}")

            while True:
                edit_task = input("What to do with this (delete, Modify) : ")

                match edit_task:
                    case "Modify"|"modify":
                        newTodo = f"{input("Enter New Todo to Override the selected task  : ")}.\n"
                        todos[num - 1] = newTodo
                        break

                    case "delete"|"Delete":
                        print(f"Deleted the selected task : {todos.pop(num-1)}")
                        break


                    case _:
                        print("Invalid Choice")

            write_todos(todos)

        except ValueError:
            print("Your Command is Not Valid")
            continue

        except IndexError:
            print("Invalid Task number, \n Please make sure task number is within the range")
            continue

    elif (user_action.startswith('complete')) | (user_action.startswith('Complete')):
        try:
            num = int(user_action[9:])
            todos = get_todo()

            print(f"Completed Task is \n{todos.pop(num-1)}")

            write_todos(todos)
        except IndexError:
            print("Invalid Task number, \n Please make sure task number is within the range")
            continue

    elif (user_action.startswith("exit")) | (user_action.startswith("Exit")):
        break

    else:
        print("Invalid Choice")

print("Bye!")
