import argparse 

def local_value_numbering(f):
    f = open(f)
    s = f.read()
    f.close()

    pre = s.split("// Start optimization range")[0]
    post = s.split("// Start optimization range")[1].split("// End optimization range")[1]
    to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]

    # hint: perform the local value numbering optimization here on to_optimize
    
    # split the block into statements
    statements = to_optimize.split(";")
    statements = [s.strip() for s in statements]
    statements = [s for s in statements if s != ""]
    
    # Variables to keep track of expressions and their assigned variables
    value_table = {} # expr -> var
    replaced = 0 # number of instructions replaced
    new_var_count = 0 # number of new variables created

    new_var_block = "" # block of new variable declarations
    optimized_block = "" # block of optimized instructions

    # Process each line in the to_optimize block
    for statement in statements:

        # Parse the instruction
        var, expr = statement.split(' = ')
        operand1, op, operand2 = expr.split(' ')

        # Check if the expression has been computed before
        if expr in value_table:
            # Replace arithmetic with assignment
            optimized_block += f"{var} = {value_table[expr]};\n"
            replaced += 1
        else:
            if op == '+':
                # Check for commutative equivalent
                commutative = f"{operand2} + {operand1}"
                if commutative in value_table:
                    # Replace arithmetic with assignment
                    optimized_block += f"{var} = {value_table[commutative]};\n"
                    replaced += 1
                    continue
            # New expression, assign to a new variable
            new_var = f"t{new_var_count}"
            new_var_count += 1
            value_table[expr] = new_var

            # Declare the new variable and add the original arithmetic line
            new_var_block += f"auto {new_var} = {expr};\n"
            optimized_block += f"{var} = {new_var};\n"
            
            
    print(pre)
    print(new_var_block)
    print(optimized_block)
    print(post)

    # Print out how many instructions were replaced
    print(f"// replaced: {replaced}")

        
    
    
    
    
    
    
    
    
    
    # print(pre)

    # hint: print out any new variable declarations you need here

    # hint: print out the optimized local block here

    # hint: store any new numbered variables back to their unumbered counterparts here
    
    # print(post)

    # You should keep track of how many instructions you replaced
    #print("// replaced: " + str(replaced))    
    

# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.
if __name__ == '__main__': 
    parser = argparse.ArgumentParser()   
    parser.add_argument('cppfile', help ='The cpp file to be analyzed') 
    args = parser.parse_args()
    local_value_numbering(args.cppfile)
