import streamlit as st
import functions


todos=functions.read_todos()
def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Todo app")
st.subheader("This is my first app")
st.write("This app is to increase your productivity")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="", placeholder="Add new todo....", on_change=add_todo, key="new_todo")