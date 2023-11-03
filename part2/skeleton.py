# Ziyuan Wang & Inje Kim

import ply.lex as lex
import ply.yacc as yacc

# Build the lexer

tokens = (
    'CHAR',
    'CONCAT',
    'UNION',
    'STAR',
    'OPTIONAL',
    'LPAREN',
    'RPAREN'
)

t_CHAR = r'[a-zA-Z0-9]'
t_CONCAT = r'\.'
t_UNION = r'\|'
t_STAR = r'\*'
t_OPTIONAL = r'\?' 
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = " \t\n"

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# RE Tree
class Node:
    pass


        
class Leaf(Node):
    def __init__(self, char):
        self.char = char

    def is_epsilon(self):
        return self.char == 'epsilon'

class Concat(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Union(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Star(Node):
    def __init__(self, child):
        self.child = child

class Optional(Node):
    def __init__(self, child):
        self.child = child
        
# Parser
precedence = (
    ('left', 'UNION'),
    ('left', 'CONCAT'),
    ('nonassoc', 'STAR', 'OPTIONAL')
)

def p_expression_union(p):
    'expression : expression UNION cat_expr'
    p[0] = Union(p[1], p[3])

# Passing down expression value for the next level
def p_expression(p):
    'expression : cat_expr'
    p[0] = p[1]

# Handling Concatenation: A . B
def p_cat_expr_concat(p):
    'cat_expr : cat_expr CONCAT star_expr'
    p[0] = Concat(p[1], p[3])
    
def p_cat_expr_implicit_concat(p):
    'cat_expr : cat_expr factor'
    p[0] = Concat(p[1], p[2])

# Passing down cat_expr value for the next level
def p_cat_expr(p):
    'cat_expr : star_expr'
    p[0] = p[1]

# Handling Kleene Star: A*
def p_star_expr_star(p):
    'star_expr : factor STAR'
    p[0] = Star(p[1])

# # Handling Optional: A?  
def p_factor_optional(p):
    'factor : factor OPTIONAL'
    p[0] = Optional(p[1])

# Passing down star_expr value for factor
def p_star_expr(p):
    'star_expr : factor'
    p[0] = p[1]

# Handling parentheses
def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Handling characters
def p_factor_char(p):
    'factor : CHAR'
    p[0] = Leaf(p[1])

# Error rule
def p_error(p):
    print(f"Syntax error at {p.value}")


## Nullable function starting here:

# Top level Nullable function: this function takes an RE (re) as an
# AST and returns:
# (1) an RE AST for the empty string (epsilon) if the re matches the empty string (epsilon).
# (2) an RE AST for the empty set if the re does NOT match the empty string.

# Implement this function
# def nullable(re):
#     pass

# derivative function starting here:

# This function takes a character (char) and an RE AST (re). It
# returns the RE (as an AST) that is the derivative of re with respect
# to char.

# More specifically: say the input RE (re) accepts the set of strings S.
# The derivative of re with respect to char is all strings in S that began
# with char, and now have char ommitted. Here are some examples:

# Given a RE (call it re) that matches the language {aaa, abb, ba, bb,
# ""}, the derivative of re with respect to 'a' is {aa, bb}. These are
# the original strings that began with 'a' (namely {aaa, abb}), with
# the first 'a' character removed. Please review the lecture or the
# "Regular-expression derivatives reexamined" for more information

# implement this function:
# def derivative_re(char, re):
#     pass

def nullable(re):
    if isinstance(re, Leaf):
        return Leaf('epsilon') if re.is_epsilon() else Leaf('empty')
    elif isinstance(re, Concat):
        left_null = nullable(re.left)
        right_null = nullable(re.right)
        return Leaf('epsilon') if left_null.is_epsilon() and right_null.is_epsilon() else Leaf('empty')
    elif isinstance(re, Union):
        left_null = nullable(re.left)
        right_null = nullable(re.right)
        return Leaf('epsilon') if left_null.is_epsilon() or right_null.is_epsilon() else Leaf('empty')
    elif isinstance(re, Star):
        return Leaf('epsilon')
    elif isinstance(re, Optional):
        return Leaf('epsilon')
    else:
        raise ValueError("Type error")

def is_epsilon(node):
    return isinstance(node, Leaf) and node.char == 'epsilon'


def derivative_re(char, re):
    if isinstance(re, Leaf):
        if re.is_epsilon():
            return Leaf('empty')
        return Leaf('epsilon') if re.char == char else Leaf('empty')
    elif isinstance(re, Concat):
        if is_epsilon(nullable(re.left)):
            return Union(Concat(derivative_re(char, re.left), re.right), derivative_re(char, re.right))
        return Concat(derivative_re(char, re.left), re.right)
    elif isinstance(re, Union):
        return Union(derivative_re(char, re.left), derivative_re(char, re.right))
    elif isinstance(re, Star):
        return Concat(derivative_re(char, re.child), Star(re.child))
    elif isinstance(re, Optional):
        return derivative_re(char, re.child)
    
    else:
        raise ValueError("Type error")



parser = yacc.yacc()

# High-level function to match a string using regular experession
# derivatives:
# def match_regex_ast(re, to_match):

#     # create the derivative for each character of the string in sequence
#     for char in to_match:
#         re =  derivative_re(char, re)

#     # the string matches if and only if the empty string is matched by the derivative RE
#     return False # you will need to write something like: is_epsilon(nullable(re)) here
# def is_epsilon(re):
#     return isinstance(re, Leaf) and re.is_epsilon()

def match_regex_ast(re, to_match):
    for char in to_match:
        re = derivative_re(char, re)
    return is_epsilon(nullable(re))

# Keep this function exactly how it is for grading to use with the tester scripts.
def match_regex(reg_ex, string):
    return match_regex_ast(parser.parse(reg_ex), string)

# Use this conditional to test your script locally
if __name__ == "__main__":
    d_re = parser.parse("helll?o")


    print(match_regex_ast(d_re, "helllo") == True)
    print(match_regex_ast(d_re, "hello") == True)

    
# # Use this conditional to test your script locally
# if __name__ == "__main__":
#     d_re = parser.parse("(h.i)* | c.s.e*.2.1.1")
#     # d_re = "(h.i)* | c.s.e*.2.1.1"

#     # should pass
#     print(match_regex_ast(d_re, "hi") == True)    
#     print(match_regex_ast(d_re, "hihi") == True)
#     print(match_regex_ast(d_re, "cse211") == True)
#     print(match_regex_ast(d_re, "cs211") == True)
#     print(match_regex_ast(d_re, "cseee211") == True)

#     # should fail
#     print(match_regex_ast(d_re, "hhh") == False)
#     print(match_regex_ast(d_re, "cseee21") == False)
#     print(match_regex_ast(d_re, "211") == False)
