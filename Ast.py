import re
import json
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"

    def modify_node(self, new_value=None, new_left=None, new_right=None):
        if new_value is not None:
            self.value = new_value
        if new_left is not None:
            self.left = new_left
        if new_right is not None:
            self.right = new_right
    
def create_rule(rule_string):
    tokens=tokenize(rule_string)

    ast=parse_tokens(tokens)
    return ast

def  tokenize(rule_string):
    token_pattern=r"(\b\w+\b|>=|<=|==|!=|>|<|\(|\)|AND|OR)"
    tokens=re.findall(token_pattern,rule_string)
    return tokens

def parse_tokens(tokens):
    stack=[]
    while tokens:
        token=tokens.pop(0)
        if token=='(':
            stack.append('(')
        elif token==')':
            right_node=stack.pop()
            operator=stack.pop()
            left_node=stack.pop()
            stack.pop()

            new_node=Node(node_type='operator',left=left_node,right=right_node,value=operator)
            stack.append(new_node)
        elif token in ('AND','OR'):
            stack.append(token)
        else:
            operand_node=create_operand_node(token,tokens)
            stack.append(operand_node)
    return stack[0]

def create_operand_node(token,tokens):
    operator=tokens.pop(0)
    value=tokens.pop(0)
    condition=(token,operator,value)
    return Node(node_type='operand',value=condition)

def evaluate_rule(node, data):
    if node.type == 'operand':
        return evaluate_condition(node.value, data)
    left_result = evaluate_rule(node.left, data)
    right_result = evaluate_rule(node.right, data)
    if node.value == 'AND':
        return left_result and right_result
    elif node.value == 'OR':
        return left_result or right_result
    else:
        raise ValueError(f"Unknown operator: {node.value}")
    
def evaluate_condition(condition, data):
    attribute, operator, value = condition
    if attribute not in data:
        raise ValueError(f"Attribute {attribute} not found in data")
    user_value = data[attribute]
    if operator == '>':
        return user_value > int(value)
    elif operator == '<':
        return user_value < int(value)
    elif operator == '>=':
        return user_value >= int(value)
    elif operator == '<=':
        return user_value <= int(value)
    elif operator == '==':
        return user_value == value
    elif operator == '!=':
        return user_value != value
    else:
        raise ValueError(f"Unknown operator: {operator}")

def combine_rules(rules, operator="AND"):
    ast_list = [create_rule(rule) for rule in rules]
    combined_ast = ast_list[0]
    for ast in ast_list[1:]:
        combined_ast = Node(node_type='operator', left=combined_ast, right=ast, value=operator)
    return combined_ast  




def validate_rule(rule_string):
   
    valid_operators = ["AND", "OR", ">", "<", "==", ">=", "<="]
    if not any(op in rule_string for op in valid_operators):
        return False, "The rule must contain valid comparison operators (e.g., >, ==)"
    

    valid_attributes = ["age", "department", "salary", "experience"]
    if not any(attr in rule_string for attr in valid_attributes):
        return False, f"The rule must contain valid attributes: {valid_attributes}"

    return True, ""

def validate_user_data(user_data):
    required_fields = ["age", "department", "salary", "experience"]
    for field in required_fields:
        if field not in user_data:
            return False, f"Missing required field: {field}"
    return True, ""



def modify_ast_node(ast_node, new_value=None, new_left=None, new_right=None):
    if new_value is not None:
        ast_node.value = new_value
    if new_left is not None:
        ast_node.left = new_left
    if new_right is not None:
        ast_node.right = new_right
    return ast_node

import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",       
        user="root",        
        password="123456", 
        database="rule_engine_db"  
    )
    return connection
def store_rule_in_db(rule_string, ast):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "INSERT INTO rules (rule_text, ast) VALUES (%s, %s)"
    cursor.execute(query, (rule_string, str(ast))) 
    connection.commit()

    cursor.close()
    connection.close()

def get_all_rules_from_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT id, rule_text, ast FROM rules"
    cursor.execute(query)
    rules = cursor.fetchall()

    cursor.close()
    connection.close()
    return rules

