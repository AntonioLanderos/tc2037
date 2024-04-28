import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
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


# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to be parsed
sentence = 'if 3 < 5 then my_variable = "Ruby" end'

# Tokenize the sentence
#tokens = nltk.word_tokenize(sentence)
tokens = sentence.split()

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()