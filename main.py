import streamlit as st
from app import run_app

def main():

    st.title("Rule Engine with Abstract Syntax Tree (AST)")
    st.write("""
        This application allows you to dynamically create and evaluate rules based on user attributes
        such as age, department, salary, and experience.
    """)
    
   
    run_app()

if __name__ == "__main__":
    main()
