import ply.lex as lex
import ply.yacc as yacc


tokens = ['NUM', 'VAR', 'PLUS', 'MINUS', 'DIV', 
              'LPAREN', 'RPAREN', 'SEMICOLON', 'EQUALS', 'FOR', 
              'IF', 'ELSE', 'WHILE', 'LB', 'RB', 'PRINT', 'INT', 
              'GREATER', 'LESS', 'IGNORE_CONTENT', 'COUT', 'SENTENCE',
              'COMMA', 'ENDL', 'RETURN','LBRACKET', 'RBRACKET', 'STAR']

# t_MULT = r'\*'
# t_PLUS = r'\+'
# t_MINUS = r'\-'
t_DIV = r'/'    
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_FOR = "for"
t_IF = "if"
t_ELSE = "else"
t_WHILE = "while"
t_COUT = r'cout'
t_ENDL = r'endl'
t_RETURN = r'return'
t_LB = r'\{'
t_RB = r'\}'
t_GREATER = r'\>'
t_LESS = r'\<'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_STAR = r'\*'
# t_DQM = r'\"'
t_COMMA = r','

def t_IGNORE_CONTENT(t):
    r'\/\/.*|\#.*|using|namespace|std;'
    pass

def  t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
t_ignore = ' '

reserved = {
    'print' : 'PRINT',
    'for' : 'FOR',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'cout' : 'COUT',
    'endl' : 'ENDL',
    'return' : 'RETURN'
}


def t_SENTENCE(t):
    r'"[\w\s,\.\:]+"'
    t.type = reserved.get(t.value, 'SENTENCE')
    return t

def t_INT(t):
    r'int'
    t.type = reserved.get(t.value, 'INT')
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')
    return t

def t_PLUS(t):
    r'\+'
    t.type = 'PLUS'
    return t

def t_MINUS(t):
    r'-'
    t.type = 'MINUS'
    return t

# def t_FOR(t):
#     r'for'
#     t.type = 'FOR'
#     return t

# def t_WHILE(t):
#     r'while'
#     t.type = 'WHILE'
#     return t

# def t_IF(t):
#     r'if'
#     t.type = 'IF'
#     return t

def t_newline(t):
    r'\n'
    t.lexer.lineno +=1
    return None

lexer = lex.lex()

# Parser

# rule for intermediate representation:

# variable declaration: ('declare', var_name, value)
# int x = 10;  ==> ('declare', 'x', '10')
# int y; ==> ('declare', 'y','0')

# variable assignment: ('assign', var_name, value)
# x = 11; ==> ('assign', 'x', '11')

# if statement: ('if', condition)
# if (sum = 10); ==> ('if', 'sum = 10')

# For loop: ('for', iter, start, end, update)
# for (int i = 0; i < 5; i++) ==> ('for', 'int i', '0', '5', 'i+1')

# while loop: ('while', condition)
# while (j = 5) ==> ('while', 'j = 5')

# print statement: ('print', string, var_name)
# cout << x; ==> ('print', '', 'x')
# cout << "Hello World"; ==> ('print', '"Hello World"', '')
# cout << "Hello World" << x; ==> ('print', '"Hello World", x)

def p_program(p):
    '''program : statement
               | program statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# ('func_declare', name, args, return_type)   
def p_func_decl(p):
    '''
    statement : INT VAR LPAREN params RPAREN SEMICOLON
    '''
    p[0] = ('func_declare', p[2], p[4], p[1])
def p_function(p):
    '''
    statement : INT VAR LPAREN params RPAREN
    '''
    p[0] = ('function', p[2], p[4], p[1])

def p_func_params(p):
    '''
    params : INT VAR
           | params COMMA INT VAR
           |
    '''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 3:
        p[0] = [(p[1], p[2])]
    else:
        p[0] = p[1] + [(p[3], p[4])]

def p_func_args(p):
    '''
    args : VAR
         | args COMMA VAR
         | NUM
         | args COMMA NUM
         |
    '''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = [(p[1])]
    else:
        p[0] = (p[1]) + [p[3]]
        
def p_f_statement(p):
    '''
    statement : f_statement
    '''
    p[0] = p[1]
        
# sum = addNumbers(x, y); ==> ('func_call', 'sum', 'addNumbers', ['x', 'y'])
def p_func_call(p):
    '''
    f_statement : VAR LPAREN args RPAREN SEMICOLON
                | VAR EQUALS f_statement
    '''
    if len(p) == 4:
        p[0] = ('func_call_assign', p[1], p[3])
    else:
        p[0] = ('func_call', p[1], p[3])

# variable declaration: ('declare', var_name, value)
# temporarily assume everything is assigned to a literal
def p_statement_decl(p):
    '''
    statement : INT VAR SEMICOLON
              | INT VAR EQUALS NUM SEMICOLON
              | INT VAR EQUALS VAR SEMICOLON
              | INT VAR EQUALS expr SEMICOLON
    '''
    if len(p) == 4:
        p[0] = ('declare', p[2], 0)
    else:
        p[0] = ('declare', p[2], p[4])

# variable assignment: ('assign', var_name, value)
def p_statement_assign(p):
    '''
    statement : VAR EQUALS NUM SEMICOLON
                | VAR EQUALS expr SEMICOLON
    '''
    p[0] = ('assign', p[1], p[3])
    
def p_statement_plusplus(p):
    '''
    statement : VAR PLUS PLUS SEMICOLON
    '''
    p[0] = ('assign', p[1], f'{p[1]} + 1')

# if statement: ('if', condition)
def p_statement_if(p):
    '''
    statement : IF LPAREN condition RPAREN
    '''
    p[0] = ('if', p[3])
    
def p_statement_if_else(p):
    '''
    statement : ELSE
    '''
    p[0] = ('else', )

# For loop: ('for', iter, start, end, update)
def p_statement_for(p):
    '''
    statement : FOR LPAREN INT VAR EQUALS NUM SEMICOLON condition SEMICOLON for_update RPAREN
    '''
    p[0] = ('for', f'int {p[4]}', p[6], p[8], p[10])
    pass

# while loop: ('while', condition)
def p_statement_while(p):
    '''
    statement : WHILE LPAREN condition RPAREN
    '''
    p[0] = ('while', p[3])
    pass

# condition
def p_condition(p):
    '''
    condition : VAR GREATER NUM
                | VAR LESS NUM
                | VAR GREATER VAR
                | VAR LESS VAR
                | VAR EQUALS EQUALS NUM
    '''
    if len(p) == 4:
        p[0] = f'{p[1]} {p[2]} {p[3]}'
    else:
        p[0] = f'{p[1]} {p[2]}{p[3]} {p[4]}'
    pass

# teturn
def p_statement_return(p):
    '''
    statement : RETURN expr SEMICOLON
    '''
    p[0] = ('return', p[2])
    pass

# for update
def p_for_update(p):
    '''
    for_update : VAR PLUS PLUS
               
    '''
    p[0] = f'{p[1]} += 1'

def p_statement_lb(p):
    '''
    statement : LB               
    '''
    p[0] = ('left_brace',)

def p_statement_rb(p):
    '''
    statement : RB             
    '''
    p[0] = ('right_brace',)

def p_expr_plus(p):
    '''
    expr : expr PLUS term
    '''
    p[0] = f'{p[1]} + {p[3]}'
    pass

# def p_expr_plus_var(p):
#     '''
#     expr : expr PLUS VAR
#     '''
#     print("p[1]", p[1])
#     print("p[3]", p[3])
#     p[0] = f'{p[1]} + {p[3]}'
#     print("p[0]", p[0])
#     pass

def p_expr_minus(p):
    '''expr : expr MINUS term'''
    p[0] = f'{p[1]} - {p[3]}'

# def p_expr_minus_var(p):
#     '''expr : expr MINUS VAR'''
#     p[0] = f'{p[1]} - {p[3]}'
    
def p_expr_term(p):
    '''expr : term'''
    p[0] = p[1]
    
def p_term_mult(p):
    '''term : term STAR factor'''
    p[0] = f'{p[1]} * {p[3]}'
    
def p_term_div(p):
    '''term : term DIV factor'''
    if p[3] == 0:
        print("divide by 0 error:")
        print("cannot divide: " + str(p[1]) + " by 0")
        exit(1)
    p[0] = f'{p[1]} / {p[3]}'
    
def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]
    
    
def p_factor_expr(p):
    '''factor : LPAREN expr RPAREN'''
    p[0] = p[2]    

def p_factor_num(p):
    '''factor : NUM'''
    p[0] = p[1]
    
def p_factor_var(p):
    '''factor : VAR'''
    p[0] = p[1] 
    
def p_factor_array(p):
    '''factor : VAR LBRACKET factor RBRACKET'''
    p[0] = f'{p[1]}[{p[3]}]'
    
def p_array_decl(p):
    '''
    statement : INT STAR VAR SEMICOLON
    '''
    p[0] = ('array_declare', p[1], p[3])

def p_print_content(p):
    '''
    p_content : LESS LESS VAR p_content
            | LESS LESS SENTENCE p_content
            | LESS LESS ENDL
            |
    '''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 4:
        p[0] = [(p[3])]
    else:
        p[0] = [(p[3])] + p[4]

def p_statement_print(p):
    '''
    statement : COUT p_content SEMICOLON

    '''
    p[0] = ('print', p[2])


def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc(debug=True)



def read_cpp_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    
    cpp_code = read_cpp_file('cpp1.cpp')
    lexer.input(cpp_code)
    # while True:
    #   tok = lexer.token()
    #   if not tok: 
    #       break      # No more input
    #   print(tok)
    p = parser.parse(cpp_code)
    for command in p:
        print(command)
    
    

