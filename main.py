import streamlit as st

import functions as f

todos = f.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)
    
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app...")
st.write("This app is awesome!")

for index, todo in enumerate(todos):
   chk_box = st.checkbox(todo, key=todo)
   if chk_box:
    todos.pop(index)
    f.write_todos(todos)
    del st.session_state[todo]
    st.rerun()

st.text_input(
    label="What's on your mind?",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo",
)

