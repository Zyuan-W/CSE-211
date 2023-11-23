import ast
import argparse
import z3

# Some example functions on how to use the python ast module:

# Given a python file, return an AST using the python ast module.
def get_ast_from_file(fname):
    f = open(fname, 'r')
    s = f.read()
    f.close()
    module_ast = ast.parse(s)
    body_ast = module_ast.body[0]    
    return body_ast

def pp_expr(node):
    # print(str(node.__class__))
    # return ast.dump(node)
    if(str(node.__class__) ==  "<class '_ast.Num'>"):
        return str(node.n)
    elif(str(node.__class__) ==  "<class '_ast.Constant'>"):
        return str(node.n)
    elif(str(node.__class__) ==  "<class '_ast.Index'>"):
        return str(pp_expr(node.value))
    elif(str(node.__class__) ==  "<class '_ast.Name'>"):
        return str(node.id)
    elif(str(node.__class__) ==  "<class '_ast.BinOp'>"):
        return str(pp_expr(node.left)) + str(pp_expr(node.op)) + str(pp_expr(node.right)) 
    elif(str(node.__class__) ==  "<class '_ast.Mult'>"):
        return '*'
    elif(str(node.__class__) ==  "<class '_ast.Add'>"):
        return '+'
    elif(str(node.__class__) ==  "<class '_ast.Div'>"):
        return '/'
    elif(str(node.__class__) ==  "<class '_ast.Sub'>"):
        return '-'
    
# Example of how to get information for the ast FOR_node
def get_loop_constraints(FOR_node):
    loop_var = FOR_node.target.id
    lower_bound = FOR_node.iter.args[0].n #pp_expr(FOR_node.iter.args[0])
    upper_bound = FOR_node.iter.args[1].n #pp_expr(FOR_node.iter.args[1])
    print(lower_bound, upper_bound)
    # return the for loop information in some structure
    return (loop_var, lower_bound, upper_bound)

# Check if an ast node is a for loop
def is_FOR_node(node):
    return str(node.__class__) == "<class '_ast.For'>"

# takes in assign node
def get_write_info(node):
    name = pp_expr(node.targets[0].value)
    index = pp_expr(node.targets[0].slice)
    return (name, index)

# takes in assign node
def get_read_info(node):
    name = pp_expr(node.value.value)
    index = pp_expr(node.value.slice)
    return (name, index)

# Top level function. Given a python file name, it parses the file,
# and analyzes it to determine if the top level for loop can be done
# in parallel.
#
# It returns True if it is safe to do the top loop in parallel,
# otherwise it returns False.
def analyze_file(fname):

    my_ast = get_ast_from_file(fname)
    # print(ast)
    loop_var, lower_bound, upper_bound = get_loop_constraints(my_ast)
    my_expr = my_ast

    while is_FOR_node(my_expr):
        my_expr = my_expr.body[0]
    print(ast.dump(my_expr))
    print(get_write_info(my_expr))
    print(get_read_info(my_expr))
    # print(ast.dump(my_ast))
    # print(my_ast.body[0])
    # print(my_ast.body[0].targets)
    # print(my_ast.body[0].value)
    # print(my_ast.body[0].targets[0].value.id)
    # print(my_ast.body[0].value.value.id)
    # print(my_ast.body[0].targets[0].slice.value)
    # write_target = my_expr.targets[0].value.id
    # read_target = my_expr.value.value.id
    # write_index = my_expr.targets[0].slice.value.id
    # read_index = my_expr.value.slice.value.n
    # print(my_expr.targets[0].slice.value.id)
    # print(my_expr.value.slice.value.n)
    # ix = Int('ix')
    # iy = Int('iy')
    # write-write
    # print(ix + iy)
    # mysolver = z3.Solver()
    # mysolver.solve(1 != 2)
    # z3.solve(ix != iy, ix >= lower_bound, ix < upper_bound, iy >= lower_bound, iy < upper_bound )
    
    # Suggested steps:
    # 1. Get loop constraints (variables and bounds)
    # 2. Get expressions for read_index and write_index
    # 3. Create constraints and check them

    # Set these variables to True if there is a write-write (ww)
    # conflict or a read-write (rw) conflict
    ww_conflict = False
    rw_conflict = False
    
    return ww_conflict, rw_conflict
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()   
    parser.add_argument('pythonfile', help ='The python file to be analyzed') 
    args = parser.parse_args()
    ww_conflict, rw_conflict = analyze_file(args.pythonfile)
    print("Does the code have a write-write conflict? ", ww_conflict)
    print("Does the code have a read-write conflict?  ", rw_conflict)
