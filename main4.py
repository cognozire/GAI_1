import streamlit as st
import subprocess

def main():
    st.title("Language Selector App")

    # Language selection dropdown
    language = st.selectbox("Choose a language:", ["English", "Finnish", "German"])
    if st.button("Translate"):
        if language == "English":
            subprocess.run(["streamlit", "run", "combine.py"])
        elif language == "Finnish":
            subprocess.run(["streamlit", "run", "main2.py"])
        elif language == "German":
            subprocess.run(["streamlit", "run", "main3.py"])

def run_main(script):
    st.info(f"Running {script}")
    # You can add additional logic to run the chosen script here
    # For now, let's just print a message
    st.write(f"Script {script} executed successfully!")

if __name__ == "__main__":
    main()
