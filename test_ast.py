from Ast import create_rule, combine_rules, evaluate_rule  

def test_create_rule():
    rule = "(age > 30 AND department == 'Sales')"
    ast = create_rule(rule)
    print("AST for rule:", ast)

def test_combine_rules():
    rules = [
        "(age > 30 AND department == 'Sales')",
        "(salary > 50000 OR experience > 5)"
    ]
    combined_ast = combine_rules(rules)
    print("Combined AST:", combined_ast)

def test_evaluate_rule():
    rule = "(age > 30 AND department == 'Sales')"
    ast = create_rule(rule)
    user_data = {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 3
    }
    result = evaluate_rule(ast, user_data)
    print("Evaluation Result:", result)


if __name__ == "__main__":
    test_create_rule()
    test_combine_rules()
    test_evaluate_rule()
