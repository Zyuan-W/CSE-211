import ast
import argparse
import z3

# Some example functions on how to use the python ast module:
var_dict = dict()

# Given a python file, return an AST using the python ast module.
def get_ast_from_file(fname):
    f = open(fname, 'r')
    s = f.read()
    f.close()
    module_ast = ast.parse(s)
    body_ast = module_ast.body[0]    
    return body_ast

def pp_expr(node, numbering=0):
    # print(str(node.__class__))
    # return ast.dump(node)
    if(str(node.__class__) ==  "<class '_ast.Num'>"):
        return node.n
    elif(str(node.__class__) ==  "<class '_ast.Constant'>"):
        return node.n
    elif(str(node.__class__) ==  "<class '_ast.Index'>"):
        return pp_expr(node.value, numbering)
    elif(str(node.__class__) ==  "<class '_ast.Name'>"):
        return var_dict[node.id][numbering]
    elif(str(node.__class__) ==  "<class '_ast.BinOp'>"):
        if(str(node.op.__class__) ==  "<class '_ast.Mult'>"):
            return pp_expr(node.left, numbering) * pp_expr(node.right, numbering) 
        if(str(node.op.__class__) ==  "<class '_ast.Add'>"): 
            return pp_expr(node.left, numbering) + pp_expr(node.right, numbering) 
        if(str(node.op.__class__) ==  "<class '_ast.Div'>"):
            return pp_expr(node.left, numbering) / pp_expr(node.right, numbering) 
        if(str(node.op.__class__) ==  "<class '_ast.Sub'>"): 
            return pp_expr(node.left, numbering) - pp_expr(node.right, numbering) 
        if(str(node.op.__class__) ==  "<class '_ast.Mod'>"): 
            return pp_expr(node.left, numbering) % pp_expr(node.right, numbering) 
        
    
# Example of how to get information for the ast FOR_node
def get_loop_constraints(FOR_node):
    loop_var = FOR_node.target.id
    lower_bound = pp_expr(FOR_node.iter.args[0])
    upper_bound = pp_expr(FOR_node.iter.args[1])
    print(lower_bound, upper_bound)
    # return the for loop information in some structure
    return (loop_var, lower_bound, upper_bound)

# Check if an ast node is a for loop
def is_FOR_node(node):
    return str(node.__class__) == "<class '_ast.For'>"

# takes in assign node
def get_write_info(node, numbering):
    # name = pp_expr(node.targets[0].value, numbering)
    index = pp_expr(node.targets[0].slice, numbering)
    return index

# takes in assign node
def get_read_info(node, numbering):
    # name = pp_expr(node.value.value, numbering)
    index = pp_expr(node.value.slice, numbering)
    return index

# Top level function. Given a python file name, it parses the file,
# and analyzes it to determine if the top level for loop can be done
# in parallel.
#
# It returns True if it is safe to do the top loop in parallel,
# otherwise it returns False.
def analyze_file(fname):

    my_ast = get_ast_from_file(fname)
    # print(ast)
    original_loop_var, lower_bound, upper_bound = get_loop_constraints(my_ast)
    my_expr = my_ast
    # print(str(None))
    while is_FOR_node(my_expr):
        loop_var, lower_bound, upper_bound = get_loop_constraints(my_expr)
        var_dict[loop_var] = [z3.Int(loop_var + '0'), z3.Int(loop_var + '1'), lower_bound, upper_bound]
        my_expr = my_expr.body[0]
    print(ast.dump(my_expr))
    # i0 = z3.Int('i0')
    # i1 = z3.Int('i1')
    write_index0 = get_write_info(my_expr, 0)
    write_index1 = get_write_info(my_expr, 1)
    read_index0 = get_read_info(my_expr, 0)
    read_index1 = get_read_info(my_expr, 1)
    print(write_index0, write_index1)
    # print(write_name0)
    print(read_index0, read_index1)
   

    # write-write
    # print(ix + iy)
    mysolver = z3.Solver()
    mysolver.add(var_dict[original_loop_var][0] != var_dict[original_loop_var][1])
    for entry in var_dict.values():
      print(entry)
      mysolver.add(entry[0] >= entry[2])
      mysolver.add(entry[1] >= entry[2])
      mysolver.add(entry[0] < entry[3])
      mysolver.add(entry[1] < entry[3])
    mysolver.add(write_index0 == write_index1)
    print(mysolver.check())
    mysolver2 = z3.Solver()
    mysolver2.add(var_dict[original_loop_var][0] != var_dict[original_loop_var][1])
    for entry in var_dict.values():
      mysolver2.add(entry[0] >= entry[2])
      mysolver2.add(entry[1] >= entry[2])
      mysolver2.add(entry[0] < entry[3])
      mysolver2.add(entry[1] < entry[3])
    mysolver2.add(write_index0 == read_index1)
    print(mysolver2.check())
    # z3.solve(ix != iy, ix >= lower_bound, ix < upper_bound, iy >= lower_bound, iy < upper_bound )
    
    # Suggested steps:
    # 1. Get loop constraints (variables and bounds)
    # 2. Get expressions for read_index and write_index
    # 3. Create constraints and check them

    # Set these variables to True if there is a write-write (ww)
    # conflict or a read-write (rw) conflict
    ww_conflict = str(mysolver.check()) == 'sat'
    rw_conflict = str(mysolver2.check()) == 'sat'
    if(ww_conflict):
        print(mysolver.model())
    if(rw_conflict):
        print(mysolver2.model())
    return ww_conflict, rw_conflict
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()   
    parser.add_argument('pythonfile', help ='The python file to be analyzed') 
    args = parser.parse_args()
    ww_conflict, rw_conflict = analyze_file(args.pythonfile)
    print("Does the code have a write-write conflict? ", ww_conflict)
    print("Does the code have a read-write conflict?  ", rw_conflict)
