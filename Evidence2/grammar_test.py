import nltk
from nltk import CFG
nltk.download('punkt')

grammar = CFG.fromstring("""
    program -> statement_list
    statement_list -> statement | statement statement_list
    statement -> expression | if_statement | while_statement | assignment
    expression -> integer | string | variable | function_call
    if_statement -> 'if' condition 'then' statement_list 'end'
    while_statement -> 'while' condition 'do' statement_list 'end'
    assignment -> variable '=' string
    condition -> integer comparisson_operator integer
    comparisson_operator -> '==' | '!=' | '<' | '>' | '<=' | '>='
    function_call -> identifier '(' argument_list ')'
    integer -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    variable -> 'id' | 'my_variable' | '_underscore_variable' | 'MyVariable' | 'CONST_VAR' | 'foo_Var'
    string -> '"Hello"' | '"123"' | '"Ruby"' | '"@#()$"' | '"\\n\\t"' | '"string:#{variable}"'
    identifier -> 'variable_name' | 'myVariable' | 'my_var' | 'CONSTANT_VAR' | 'foo_bar'
    argument_list -> expression | expression ',' argument_list
""")

parser = nltk.ChartParser(grammar)

test_cases = [
    ("Accepted", 'if 3 < 5 then my_variable = "Ruby" end'),
    ("Accepted", 'while 3 <= 9 do id = "Hello" end'),
    ("Accepted", 'id = "Hello"'),
    ("Accepted", 'my_variable = "string:#{variable}"'),
    ("Rejected", 'if 3 5 then my_variable = "Ruby" end'),  # Missing comparison operator
    ("Rejected", 'while 3 9 do id = "Hello" end'),  # Missing comparison operator
    ("Rejected", 'variable_name myVariable , foo_bar'),  # Incorrect function call syntax
    ("Rejected", 'if 5 6 then MyVariable = "string:#{variable}" end'),  # Missing comparison operator
]

def test_grammar(sentence):
    tokens = sentence.split()
    try:
        trees = list(parser.parse(tokens))
        if trees:
            print("Accepted: ", sentence)
            for tree in trees:
                tree.pretty_print()
        else:
            print("Rejected: ", sentence)
    except ValueError as e:
        print("Rejected: ", sentence)

for result, sentence in test_cases:
    print(f"Expected {result}:")
    test_grammar(sentence)
    print()