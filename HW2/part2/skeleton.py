# Pranav Vempati & Ziyuan Wang

# skeleton file for UCSC CSE211 Homework 2: part 1

from pycfg.pycfg import PyCFG, CFGNode, slurp 
import argparse 
import re

iter_counter = 0
# Acks: I used
# https://www.geeksforgeeks.org/draw-control-flow-graph-using-pycfg-python/
# to get started with PyCFG. 

# Given a node, returns the instruction as a string
# instructions are of the form:
def get_node_instruction(n):
    return n.attr["label"]

# Given a CFG and a node, return a list of successor nodes
def get_node_successors(CFG, n):
    return CFG.successors(n)

# use PyCFG to get a CFG of the python input file.  Graph is returned
# as a PyGraphviz graph.  Don't worry too much about this function. It
# just uses the PyCFG API
def get_graph(input_file):
    cfg = PyCFG()
    cfg.gen_cfg(slurp(input_file).strip())
    arcs = []
    return CFGNode.to_graph(arcs)

# Helper function to extract variables from an assignment instruction
def extract_variables_from_assignment(instruction):
    # print("instruction: ", instruction)
    if '=' in instruction:
        lhs,rhs = instruction.split('=')
        lhs = lhs.strip()
        rhs = rhs.strip()
        # no_, left_var = lhs.split(' ')
        parts = lhs.split(':')
        left_var = parts[-1].strip()
        if rhs != "input()":
            return left_var, rhs
        return left_var, None
    elif "start" in instruction or "stop" in instruction:
        return None, None
    else:
        if ':' in instruction:
            parts = instruction.split(":")
            rhs = parts[-1].strip()
            return None, rhs
        return None, None

# Function to create the per-node sets of UEVar and VarKill
def create_sets(instruction):
    left_var, right_vars = extract_variables_from_assignment(instruction)
    
    # print("left_var: ", left_var, "  |  right_vars: ", right_vars)
    
    # Upward Exposed Variables are those that are used before being defined in the node. They are used interchangeably with right_vars
    UEVar = {right_vars} if right_vars else set()
    
    # Killed Variables are those that are defined and reassigned in the node. This corresponds to variables on the left hand side of assignment. 
    VarKill = {left_var} if left_var else set()
    
    # Remove killed variables from UEVar
    UEVar -= VarKill

    return UEVar, VarKill

# perform postorder traversal of the CFG
def postorder_traversal(CFG):
    visited = set()
    postorder_list = []
    
    def visit(node):
        if node not in visited:
            visited.add(node)
            for successor in get_node_successors(CFG,node):
                visit(successor)
            postorder_list.append(node)
    entry_node = next(n for n in CFG.nodes() if CFG.in_degree(n) == 0)
    visit(entry_node)
    # visit(CFG.get_node(0)) # Start at the start node
    
    return postorder_list

# You can use get_node_successors(C FG, n) to get a list of n's
# successor nodes.
def compute_LiveOut(CFG):
    global iter_counter
    # reverse_CFG = CFG.reverse()
    iter_counter = 0
    LiveOut = {n : set() for n in CFG.nodes()}
    # LiveOut = {n : set() for n in postorder_traversal(CFG)}
    UEVar = {}
    VarKill = {}
    
    postorder_nodes = postorder_traversal(CFG)
    # postorder_nodes = postorder_traversal(reverse_CFG) # rpo with reverse CFG
    # rpo_nodes = list(reversed(postorder_nodes))

    # print("rpo_nodes: ", rpo_nodes)
    # First, create per-node UEVar and VarKill sets(Part 2.1)
    for node in CFG.nodes():
    # for node in rpo_nodes:
        instruction = get_node_instruction(node)
        
        # print("instruction: ", instruction)
        UEVar[node], VarKill[node] = create_sets(instruction) # Create per-node upward exposed and killed sets
  
  
    changed = True # Flag - has there been a change in LiveOut?

    # Iterate until no changes(fixpoint algorithm)(Part 2.2)
    while changed:
        # print out the current LiveOut sets
        # for node in CFG.nodes():
        #     print(f"LiveOut[{node}]: {LiveOut[node]}")
        # print("")
        
        iter_counter += 1
        changed = False
        for node in list(CFG.nodes()): # default order
        # for node in rpo_nodes: # reverse postorder
            current_LiveOut = LiveOut[node].copy()
            # print("current_LiveOut: ", current_LiveOut)

            # Compute new LiveOut value 
            for successor in get_node_successors(CFG, node):
                LiveOut[node] |= (UEVar[successor] | (LiveOut[successor] - VarKill[successor]))

            # Check if LiveOut changed
            if current_LiveOut != LiveOut[node]:
                changed = True

    print(f"iterations: {iter_counter}")
    return LiveOut


# The uninitialized variables are the LiveOut variables from the start
# node. It is fine if your implementation needs to change this
# function. It simply needs to return a set of uninitialized variables
def get_uninitialized_variables_from_LiveOut(CFG, LiveOut):
    return LiveOut[CFG.get_node(0)]
    # entry_node = next(n for n in CFG.nodes() if CFG.in_degree(n) == 0)
    # return LiveOut[entry_node]

# The testing function. Keep the signature of this function the
# same as it will be used for grading. I highly recommend you keep the
# function exactly the same and simply implement the constituent
# functions.
def find_undefined_variables(input_python_file):

    # Convert the python file into a CFG
    CFG = get_graph(input_python_file)


    # Get LiveOut
    LiveOut = compute_LiveOut(CFG)


    # Return a set of unintialized variables
    return get_uninitialized_variables_from_LiveOut(CFG, LiveOut)



# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.
if __name__ == '__main__': 
    parser = argparse.ArgumentParser()   
    parser.add_argument('pythonfile', help ='The python file to be analyzed') 
    args = parser.parse_args()
    print(find_undefined_variables(args.pythonfile))
    

'''
Comment with observations(traversal order and effect on iterations): 

The number of iterations for each of the three traversal orders(default, rpo, and rpo on the reversed CFG) are indicated below. 

The standard rpo performs comparably to the default traversal order, and worse(in the sense of requiring more iterations) when a loop is present, as in test 6 of the provided tests. 
In that case, rpo visits the children before the parents, leading to delayed propagation(as parents are visited only after their children are updated, compounded by the loop. 

The rpo traversal performed on the reversed CFG, by contrast, exhibits a marked improvement and reduction in iterations across the tests. For test 6 in particular, rpo on the reverse CFG realizes an almost 3x reduction in iterations. 

Below are the results for all three traversal configurations. 

'''




# default order 
# iterations: 2
# passed test: 0
# ---
# iterations: 5
# passed test: 1
# ---
# iterations: 5
# passed test: 2
# ---
# iterations: 6
# passed test: 3
# ---
# iterations: 7
# passed test: 4
# ---
# iterations: 6
# passed test: 5
# ---
# iterations: 8
# passed test: 6
# ---
# iterations: 8
# passed test: 7
# ---

# rpo
# iterations: 2
# passed test: 0
# ---
# iterations: 5
# passed test: 1
# ---
# iterations: 5
# passed test: 2
# ---
# iterations: 6
# passed test: 3
# ---
# iterations: 7
# passed test: 4
# ---
# iterations: 6
# passed test: 5
# ---
# iterations: 9
# passed test: 6
# ---
# iterations: 8
# passed test: 7
# ---

# rpo with reverse CFG
# iterations: 2
# passed test: 0
# ---
# iterations: 2
# passed test: 1
# ---
# iterations: 2
# passed test: 2
# ---
# iterations: 3
# passed test: 3
# ---
# iterations: 3
# passed test: 4
# ---
# iterations: 3
# passed test: 5
# ---
# iterations: 3
# passed test: 6
# ---
# iterations: 3
# passed test: 7
# ---