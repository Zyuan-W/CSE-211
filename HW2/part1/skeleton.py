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
    expr_table = {} # expr -> var
    var_table = {} # var -> value
    replaced = 0 # number of instructions replaced
    new_var_count = 0 # number of new variables created

    new_var_block = "" # block of new variable declarations
    optimized_block = "" # block of optimized instructions

    # Process each line in the to_optimize block
    for statement in statements:

        # Parse the instruction
        var, expr = statement.split(' = ')
        var1, op, var2 = expr.split(' ') # b + c        

        if var1 in var_table:
            var1 = var_table[var1]
        # else:
        #     new_var = f"t{new_var_count}"
        #     var_table[var1] = new_var
        #     new_var_block += f"double {new_var} = {var1};\n"
        #     var1 = new_var
        #     new_var_count += 1
        
        if var2 in var_table:  
            var2 = var_table[var2]
        # else:
        #     new_var = f"t{new_var_count}"
        #     var_table[var2] = new_var
        #     new_var_block += f"double {new_var} = {var2};\n"
        #     var2 = new_var
        #     new_var_count += 1
            
        new_var_0 = f"t{new_var_count}"
        var_table[var] = new_var_0
        new_var_block += f"double {new_var_0} = {var};\n"
        var = new_var_0
        new_var_count += 1
        
        
        
        expr = f"{var1} {op} {var2}"
        # print(f"{var} = {expr}")
        # print("=====================================")
        
     
        
            


        # Check if the expression has been computed before
        if expr in expr_table:
            # Replace arithmetic with assignment
            optimized_block += f"double {var} = {expr_table[expr]};\n"
            replaced += 1
        else:
            if op == '+':
                # Check for commutative equivalent a + b = b + a
                commutative = f"{var2} + {var1}"
                if commutative in expr_table:
                    # Replace arithmetic with assignment
                    optimized_block += f"double {var} = {expr_table[commutative]};\n"
                    replaced += 1
                    continue
            # New expression, assign to a new variable
            # new_var = f"t{new_var_count}"
            # new_var_count += 1
            expr_table[expr] = var

            # Declare the new variable and add the original arithmetic line
            # new_var_block += f"auto {new_var} = {expr};\n"
            optimized_block += f"double {var} = {expr};\n"
   
            
    print(pre)
    # print("=====================================")
    # print(var_table)
    # print("=====================================")
    # print(new_var_block) # declare new variables
    print(optimized_block)
    # assign values back to original variables
    for var, value in var_table.items():
        print(f"{var} = {value};")
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
