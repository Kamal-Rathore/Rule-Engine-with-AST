import streamlit as st
import json
from Ast import create_rule, combine_rules, evaluate_rule, store_rule_in_db, get_all_rules_from_db

def run_app():
    st.title("Rule Engine with AST")

   
    st.header("Create a Rule")
    rule_input = st.text_input("Enter a rule string (e.g., age > 30 AND department == 'Sales')")

    if st.button("Create Rule"):
        if rule_input:
            try:
                ast = create_rule(rule_input)
                st.write(f"Generated AST: {ast}")
                store_rule_in_db(rule_input, ast)
                st.success("Rule stored successfully.")
            except Exception as e:
                st.error(f"Error creating rule: {e}")
        else:
            st.warning("Please enter a valid rule string.")

    
    st.header("Combine Multiple Rules")
    rules_input = st.text_area("Enter multiple rules, each rule on a new line")
    combine_operator = st.selectbox("Select the operator to combine rules", ["AND", "OR"])

    if st.button("Combine Rules"):
        rules_list = rules_input.splitlines()
        if rules_list and all(rules_list):
            try:
                combined_ast = combine_rules(rules_list, operator=combine_operator)
                st.session_state.combined_ast = combined_ast
                st.write(f"Combined AST: {combined_ast}")
            except Exception as e:
                st.error(f"Error combining rules: {e}")
        else:
            st.warning("Please enter valid rule strings.")


    st.header("Evaluate Rule")
    user_data_input = st.text_area("Enter user data as JSON (e.g., {\"age\": 35, \"department\": \"Sales\", \"salary\": 60000})")

    if st.button("Evaluate Rule"):
        if user_data_input:
            try:
                user_data = json.loads(user_data_input)
                if 'combined_ast' in st.session_state:
                    result = evaluate_rule(st.session_state.combined_ast, user_data)
                    st.write(f"Evaluation Result: {result}")
                else:
                    st.error("Please create or combine rules before evaluating.")
            except json.JSONDecodeError:
                st.error("Invalid JSON format. Please enter valid user data.")
            except Exception as e:
                st.error(f"Error evaluating rule: {e}")
        else:
            st.warning("Please enter valid user data.")

if __name__ == "__main__":
    run_app()
