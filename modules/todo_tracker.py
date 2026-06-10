import streamlit as st
import database

def render_todo_tracker():
    st.header("✅ Daily To-Do List")
    st.write("Stay organized and focused on your daily goals.")

    # Add Todo
    with st.form("todo_form", clear_on_submit=True):
        new_task = st.text_input("Add a new task...")
        submit = st.form_submit_button("Add Task")
        if submit and new_task:
            database.add_todo(new_task)
            database.log_activity() # Log activity for streak
            st.rerun()

    # List Todos
    todos = database.get_todos()
    
    if not todos:
        st.info("Your to-do list is empty. Add a task to get started!")
    else:
        for todo in todos:
            col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
            with col1:
                is_done = st.checkbox("Done", value=bool(todo['is_done']), key=f"todo_{todo['id']}", label_visibility="collapsed")
                if is_done != bool(todo['is_done']):
                    database.update_todo(todo['id'], int(is_done))
                    database.log_activity()
                    st.rerun()
            with col2:
                # Strike-through if done
                task_text = f"~~{todo['task']}~~" if todo['is_done'] else todo['task']
                st.write(task_text)
            with col3:
                if st.button("🗑️", key=f"del_{todo['id']}"):
                    database.delete_todo(todo['id'])
                    st.rerun()
