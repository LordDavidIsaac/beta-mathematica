import streamlit as st
import os

# --- Page Configuration ---
st.set_page_config(page_title="Beta Mathematica", layout="wide")

st.title("📘 Beta Mathematica - Academic Platform")

# --- Sidebar Navigation ---
st.sidebar.title("📚 Navigation")

sections = {
    "Notes": "notes",
    "Assignments": "assignments",
    "Writings": "writings"
}

selection = st.sidebar.radio("Select Section", list(sections.keys()))
folder = sections[selection]

# --- List Markdown Files in Selected Folder ---
try:
    files = os.listdir(folder)
    files = [f for f in files if f.endswith(".md")]
except FileNotFoundError:
    st.error(f"The folder '{folder}' does not exist.")
    files = []

# --- Search Bar to Filter Files ---
search_term = st.sidebar.text_input("🔍 Search files")

filtered_files = [f for f in files if search_term.lower() in f.lower()]

if not filtered_files:
    st.warning("No files match your search.")
else:
    selected_file = st.sidebar.selectbox("Choose File", filtered_files)
    # --- Read and Render Markdown Content ---
    try:
        with open(os.path.join(folder, selected_file), "r", encoding="utf-8") as f:
            content = f.read()
        st.markdown(content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"File '{selected_file}' not found.")

# --- FUTURE IMPROVEMENTS ---
# TODO: Add ability to upload new markdown files through the app UI.
# TODO: Add user authentication for content management.
# TODO: Implement full-text search inside markdown contents, not just filenames.
# TODO: Add PDF export or printing feature for notes and assignments.
# TODO: Add interactive quizzes or math widgets.
# TODO: Style with custom CSS or Streamlit theme enhancements.
