# import ply.lex as lex

# # You don't need to implement any more of these
# # exceptions; just throw them when required.
# class SymbolTableException(Exception):
#     pass

# class ParsingException(Exception):
#     pass

# # Implement this class, i.e. provide some class members and implement
# # the functions.
# class SymbolTable:

#     def __init__(self):
#         pass
    
#     def insert(self,name,value):
#         pass

#     def lookup(self, name):
#         pass
    
#     def push_scope(self):
#         pass

#     def pop_scope(self):
#         pass

# # define tokens here
# tokens = ['NUM', 'VAR', 'INCREMENT', "MULT", 'PLUS', 'MINUS', 'DIV', 'EQUAL', 'LPAR', 'RPAR', 'SEMI', 'LB', 'RB', 'TYPE', 'PRINT']

# lexer = lex.lex()

# #define production rules here

# parser = yacc.yacc(debug=True)

# # Global variables I suggest you use (although you are not required)
# to_print = []
# ST = SymbolTable()

# def parse_string(s):
#     global to_print
#     global ST
#     ST = SymbolTable()
#     to_print = []
#     parser.parse(s)
#     return to_print
    
# # Example on how to test locally in this file:

# #parser.parse("""
# #x = 5 + 4 * 5;
# #i = 1 + 1 * 0;
# #print(i);
# #{
# #  l = 5 ^ x;
# #{
# #    k = 5 + 7;
# #}
# #}
# #q = x / i;
# #print(q);
# #""")

# #for p in to_print:
# #    print(p)


import ply.lex as lex
import ply.yacc as yacc

# You don't need to implement any more of these
# exceptions; just throw them when required.
class SymbolTableException(Exception):
    pass

class ParsingException(Exception):
    pass

# Implement this class, i.e. provide some class members and implement
# the functions.
class SymbolTable:

    def __init__(self):
        self.table = []

    def insert(self, name, value):
        self.table.append((name, value))

    def lookup(self, name):
        for entry in reversed(self.table):
            if entry[0] == name:
                return entry[1]
        return None

    def push_scope(self):
        self.table.append('{')

    def pop_scope(self):
        while self.table[-1] != '{':
            self.table.pop()
        self.table.pop()

# define tokens here
tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EXPONENT',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMI'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\^'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()


# Ignored characters
t_ignore = " \t"

lexer = lex.lex()

#define production rules here
# Basic expression rules
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EXPONENT expression
                  | NUMBER
                  | ID'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

# Assignment
def p_assignment(p):
    '''statement : ID EQUALS expression SEMI'''
    global ST
    ST.insert(p[1], p[3])
    p[0] = ("ASSIGN", p[1], p[3])

# Print statement
def p_print(p):
    '''statement : PRINT LPAREN ID RPAREN SEMI'''
    global to_print, ST
    value = ST.lookup(p[3])
    if value is None:
        raise ParsingException(f"Variable {p[3]} not found!")
    to_print.append(value)

# Scope
def p_scope(p):
    '''scope : LBRACE statements RBRACE'''
    p[0] = p[2]

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_error(p):
    raise ParsingException(f"Syntax error at '{p.value}'")

parser = yacc.yacc(debug=True)

# Global variables I suggest you use (although you are not required)
to_print = []
ST = SymbolTable()

def parse_string(s):
    global to_print
    global ST
    ST = SymbolTable()
    to_print = []
    parser.parse(s)
    return to_print

# # Example on how to test locally in this file:

# parser.parse("""
# x = 5 + 4 * 5;
# i = 1 + 1 * 0;
# print(i);
# {
#  l = 5 ^ x;
# {
#    k = 5 + 7;
# }
# }
# q = x / i;
# print(q);
# """)
parser.parse("""
x = 5 + 4 * 5;
i = 1 + 1 * 0;
print(x)
print(i)
""")

for p in to_print:
   print(p)
