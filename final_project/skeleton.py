import ply.lex as lex
import ply.yacc as yacc


tokens = ['NUM', 'VAR', 'MULT', 'PLUS', 'MINUS', 'DIV', 
              'LPAREN', 'RPAREN', 'SEMICOLON', 'EQUALS', 'FOR', 
              'IF', 'ELSE', 'WHILE', 'LB', 'RB', 'PRINT', 'INT']

t_MULT = r'\*'
# t_PLUS = r'\+'
# t_MINUS = r'-'
t_DIV = r'/'    
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_FOR = "for"
t_IF = "if"
t_ELSE = "else"
t_WHILE = "while"
t_LB = r'\{'
t_RB = r'\}'

def  t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
t_ignore = ' '

reserved = {
    'print' : 'PRINT',
    'for' : 'FOR',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE'
}

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

lex = lex.lex()

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

def p_program(p):
    '''program : statement
               | program statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
        
        
# variable declaration: ('declare', var_name, value)
def p_statement_decl(p):
    pass

# variable assignment: ('assign', var_name, value)
def p_statement_assign(p):
    pass

# if statement: ('if', condition)
def p_statement_if(p):
    pass

# For loop: ('for', iter, start, end, update)
def p_statement_for(p):
    pass

# while loop: ('while', condition)
def p_statement_while(p):
    pass

# condition
def p_condition(p):
    pass





def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()



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
    
    cpp_code = read_cpp_file('cpp_code.cpp')
    parser.parse(cpp_code)
    
    

