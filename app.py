import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="30 Days of Streamlit Checklist",
    page_icon="📅",
    layout="centered"
)

# Title
st.title("📅 30 Days of Streamlit Checklist")
st.write("""
Welcome to the **30 Days of Streamlit Challenge**! Use this app to track your progress and ensure you stay on schedule.
""")

# Sidebar for Instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
- **Mark tasks as complete**: Check off each app as you finish it.
- **Progress Tracker**: View your completion percentage at the top.
- **Daily Goals**: Refer to the checklist for app ideas.
""")

# Data Initialization
if "tasks" not in st.session_state:
    # Define default tasks
    st.session_state.tasks = [
        {"Day": i + 1, "App Idea": idea, "Completed": False}
        for i, idea in enumerate([
            "Hello World (Input and Output)",
            "Data Table Viewer",
            "Line Chart Demo",
            "File Uploader App",
            "Text Analysis Tool",
            "Markdown Renderer",
            "Simple Calculator",
            "To-Do List App",
            "Poll Creator",
            "Budget Planner",
            "Weather Dashboard (API Integration)",
            "Image Uploader and Resizer",
            "Fitness Tracker",
            "Recipe Manager",
            "COVID-19 Stats Dashboard",
            "Stock Price Tracker",
            "Movie Recommender",
            "Cryptocurrency Watchlist",
            "Sentiment Analysis (NLP)",
            "AI Chatbot using OpenAI or Ollama",
            "Interactive Map Viewer",
            "Machine Learning Prediction App",
            "Dynamic Data Visualizations",
            "Task Manager with Database",
            "Custom ML Model Deployment",
            "Image Recognition App",
            "Real-time Data Streams",
            "E-Commerce Dashboard",
            "Portfolio App",
            "Showcase App with Links"
        ])
    ]

# Convert tasks to DataFrame for display
df = pd.DataFrame(st.session_state.tasks)

# Progress Tracker
completed_tasks = df["Completed"].sum()
total_tasks = len(df)
completion_rate = (completed_tasks / total_tasks) * 100

st.metric("Progress", f"{completed_tasks} / {total_tasks} Apps Completed", f"{completion_rate:.1f}%")

# Display Checklist
st.subheader("Checklist")
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([1, 9])
    with col1:
        # Checkbox for completion
        checked = st.checkbox("", key=f"task_{i}", value=task["Completed"])
        st.session_state.tasks[i]["Completed"] = checked
    with col2:
        st.write(f"**Day {task['Day']}:** {task['App Idea']}")

# Button to Reset Progress
if st.button("Reset Progress"):
    for task in st.session_state.tasks:
        task["Completed"] = False
    st.experimental_rerun()

st.write("---")
st.write("Stay consistent and good luck! 🚀")
