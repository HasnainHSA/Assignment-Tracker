import streamlit as st
from datetime import datetime
import json
import os
import matplotlib.pyplot as plt
from collections import defaultdict


st.markdown("""
    <head>
        <link rel="shortcut icon" href="./favicon.ico" type="image/x-icon">
    </head>
    <style>
    .stApp {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        color: #e0e0e0;
    }
    h1 {
        color: #ffffff;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    h2 {
        color: #bdc3c7;
        font-size: 24px;
        margin-top: 20px;
    }
    
    .stTextInput > div > div > input {
        background-color: #2c2c2c;
        border: 2px solid #444444;
        border-radius: 8px;
        padding: 8px;
        color: #e0e0e0;
        transition: border-color 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #00b4d8;
        outline: none;
    }
    .stDateInput > div > div > input {
        background-color: #2c2c2c;
        border: 2px solid #444444;
        border-radius: 8px;
        color: #e0e0e0;
    }
    .stButton > button {
        background-color: #00b4d8;
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #00d4ff;
        box-shadow: 0 0 8px rgba(0, 212, 255, 0.6);
        transform: translateY(-2px);
    }
    .stCheckbox > label {
        color: #e0e0e0;
        font-size: 16px;
    }
    .stProgress > div > div > div {
        background-color: #27ae60;
        transition: width 0.5s ease-in-out;
    }
    .assignment-item {
        background-color: #2c2c2c;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
        animation: fadeIn 0.5s ease-in;
    }
    .overdue {
        color: #e74c3c;
        font-weight: bold;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        margin-top: 30px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app setup
st.title("🧾Assignment Tracker")
st.write("Track your uni Assignments with their due dates.")

# File to store 
ASSIGNMENT_FILE = "assignments.json"


def load_assignments():
    if os.path.exists(ASSIGNMENT_FILE):
        try:
            with open(ASSIGNMENT_FILE, "r") as f:
                data = json.load(f)
                assignments = data.get("assignments", {})
                history = data.get("history", [])
                for name, details in assignments.items():
                    details["due_date"] = datetime.strptime(details["due_date"], "%Y-%m-%d").date()
                return assignments, history
        except json.JSONDecodeError:
            st.warning("No assignment is added")
            return {}, []
    return {}, []



def save_assignments(assignments, history):
    save_data = {
        "assignments": {name: {"due_date": details["due_date"].strftime("%Y-%m-%d"), "completed": details["completed"]}
                        for name, details in assignments.items()},
        "history": history
    }
    with open(ASSIGNMENT_FILE, "w") as f:
        json.dump(save_data, f)


if "assignments" not in st.session_state or "history" not in st.session_state:
    st.session_state.assignments, st.session_state.history = load_assignments()



st.subheader("Add Assignment")
with st.form(key="add_assignment_form"):
    assignment_name = st.text_input("Assignment Name (e.g., 'ITSE Lab' )")
    due_date = st.date_input("Due Date", min_value=datetime.today())
    submit_button = st.form_submit_button(label="Add Assignment")
    
    if submit_button and assignment_name and due_date:
        if assignment_name not in st.session_state.assignments:
            st.session_state.assignments[assignment_name] = {
                "due_date": due_date,
                "completed": False
            }
            st.session_state.history.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "action": "added",
                "name": assignment_name
            })
            save_assignments(st.session_state.assignments, st.session_state.history)
            st.success(f"Added '{assignment_name}' due {due_date.strftime('%Y-%m-%d')}!")

# Display assignments
st.subheader("Your Assignments")
if st.session_state.assignments:
    sorted_assignments = dict(sorted(st.session_state.assignments.items(), key=lambda x: x[1]["due_date"]))
    
    for name, details in sorted_assignments.items():
        days_left = (details["due_date"] - datetime.today().date()).days
        overdue = days_left < 0
        
        st.markdown(f"""
            <div class="assignment-item">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>{name} - Due: {details['due_date'].strftime('%Y-%m-%d')} 
                        <span class="{'overdue' if overdue else ''}">
                            ({'Overdue!' if overdue else f'{days_left} days left'})
                        </span>
                    </span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            completed = st.checkbox("Done", value=details["completed"], key=f"check_{name}")
            if completed != details["completed"]:
                st.session_state.assignments[name]["completed"] = completed
                if completed:

                    st.session_state.history.append({
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "action": "completed",
                        "name": name
                    })
                save_assignments(st.session_state.assignments, st.session_state.history)
        with col2:
            if st.button("Delete", key=f"del_{name}"):
                del st.session_state.assignments[name]
                st.session_state.history.append({
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "action": "deleted",
                    "name": name
                })
                save_assignments(st.session_state.assignments, st.session_state.history)
                st.success(f"Deleted '{name}'!")
                st.rerun()



    st.subheader("Progress Breakdown")
    total_assignments = len(st.session_state.assignments)
    completed_assignments = sum(1 for details in st.session_state.assignments.values() if details["completed"])
    progress = completed_assignments / total_assignments if total_assignments > 0 else 0
    
    st.write(f"Completed: {completed_assignments} / Total: {total_assignments}")
    st.progress(progress)
    
    # Charts
    if st.session_state.history:
        labels = ["Completed", "Pending"]
        sizes = [completed_assignments, total_assignments - completed_assignments]
        colors = ["#27ae60", "#e74c3c"]
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        ax2.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90, textprops={"color": "#e0e0e0"})
        ax2.axis("equal")
        ax2.set_title("Current Status", color="#e0e0e0")
        fig2.patch.set_facecolor("#1e1e1e")
        st.pyplot(fig2)



    if st.button("Clear All Assignments"):
        st.session_state.assignments.clear()
        st.session_state.history.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": "cleared_all",
            "name": "All"
        })
        save_assignments(st.session_state.assignments, st.session_state.history)
        st.success("All assignments cleared—fresh start!")

else:
    st.write("No assignments yet—add one to get started!")



st.markdown('<div class="footer">All rights reserved to  <a href="https://github.com/HasnainHSA"> HasnainHSA<a> uni vibes! 📚</div>', unsafe_allow_html=True)