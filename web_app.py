import streamlit as st
import functions

todos = functions.get_todo()

def add_todo():
    todo = st.session_state["new_todo"]+".\n"
    todos.append(todo)
    functions.write_todos(todos)

def complete_todo(completeTask):
    todos.pop(todos.index(completeTask))
    functions.write_todos(todos)
    del st.session_state[completeTask]
    st.rerun()

st.title("My To-Do App")
st.subheader("This web-app helps improve your Productivity")

for index,todo in enumerate(todos):
    check = st.checkbox(todo,key = todo)
    if check:
        complete_todo(todo)

st.text_input(label="",placeholder = "Add New ToDo....",
              on_change=add_todo,key = "new_todo")

