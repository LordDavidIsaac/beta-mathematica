import streamlit as st
import os

# Page configuration
st.set_page_config(page_title="Beta Mathematica", layout="wide")
st.title("📘 Beta Mathematica - Academic Platform")

# Sidebar Navigation
st.sidebar.title("📚 Navigation")

sections = {
    "Notes": "notes",
    "Assignments": "assignments",
    "Writings": "writings"
}

# Choose section and file
selection = st.sidebar.radio("Select Section", list(sections.keys()))
folder = sections[selection]

files = os.listdir(folder)
files = [f for f in files if f.endswith(".md")]

if not files:
    st.warning("No files found in this section.")
else:
    selected_file = st.sidebar.selectbox("Choose File", files)
    with open(os.path.join(folder, selected_file), "r", encoding="utf-8") as f:
        content = f.read()
    st.markdown(content, unsafe_allow_html=True)
