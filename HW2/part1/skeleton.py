# This part of the assignment is to implement local value numbering.
# We will be iterating over a basic block that consists of arithmetic operations, 
# and replacing redundant arithmetic instructions with assignment instructions.
# Your goal is to replace as many as arithmetic instructions as possible.

# the test case have a basic block delimited by comments for example:
# // Start optimization range
# c = h - f;
# c = e + h;
# a = f + h;
# a = f - e;
# // End optimization range

# You will need to iterate over each statement in the basic block. You can assume statements are limited to the following form:
# var = var op var;
# where var is a single lower-case character and op is either plus or minus (+ or -).
# The code that your program prints should be able to be compiled and executed. You should create as many extra variables as you need (i.e., for the numbered variables), but you are responsible
# for declaring the variables.
# Please also print out a comment at the end of your output file that states how many instructions
# were replaced. For each test case, the expected replaced instructions is shown in a comment at the top.

import argparse 

def local_value_numbering(f):
    f = open(f)
    s = f.read()
    f.close()

    pre = s.split("// Start optimization range")[0]
    post = s.split("// Start optimization range")[1].split("// End optimization range")[1]
    to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]

    # hint: perform the local value numbering optimization here on to_optimize

    # iterate over each statement in the basic block
    # statements are limited to the form: var = var op var;
    # where var is single lower-case character and op is either + or -
    
    # hint: you can use the following code to split the basic block into statements
    statements = to_optimize.split(";")
    statements = [s.strip() for s in statements]
    statements = [s for s in statements if s != ""]
    # print(statements)
    
    # Initialize variables to hold the optimized code and track seen and new variables
    optimized_code = ""
    value_number_table = {}
    expression_table = {}
    replaced = 0
    all_variables = set()
    new_variables = set()
    
    for statement in statements:
        print(f"processing {statement}")
        operation = statement.split(" = ")
        left = operation[0]
        right = operation[1]
        
        # Track all variables
        all_variables.add(left)
        all_variables.update(right.split(" "))
        
        right_0 = right
        op = right.split(" ")
        if len(op) == 3 and op[1] == "-":
            if op[0] == op[2]:
                zero = "0"
                right_0 = zero
                

        
        # Check if the expression or its commutative equivalent is already in the table
        if right_0 in expression_table:
            print(f"'{right}' already in expression table")
            # check if expressiont_table[right] is in value_number_table
            variable = expression_table[right_0]
            if variable in value_number_table:
                expre = value_number_table[variable]
                if expre == right_0:
                    optimized_code += f"{left} = {variable};\n"
                    print(f"optimized code: ")
                    print(optimized_code)
                    print("=============================================================")
                    replaced += 1
                else:
                    # get out of this if statement
                    print(f"expression table and value number table are inconsistent")
                    print(f"value_number_table: {value_number_table}")
                    print("=======================")
                    print(f"expression_table: {expression_table}")
                    print("=======================")
                    optimized_code += f"{left} = {right};\n"
                    print(f"optimized code: ")
                    print(optimized_code)
                    print("=============================================================")
                    continue
                    # print(f"expression table and value number table are inconsistent")
                
            
            # optimized_code += f"{left} = {expression_table[right]};\n"
            # print(f"optimized code: {optimized_code}")
            # print("=======================================")
            # replaced += 1
        else:
            # Check for commutative equivalent
            # print(f"'{right}' not in expression table")
            operands = right.split(" ")
            if len(operands) == 3 and operands[1] == "+":
                commutative_rhs = f"{operands[2]} + {operands[0]}"
                if commutative_rhs in expression_table:
                    # print(f"'{commutative_rhs}' is commutative equivalent of '{right}'")
                    optimized_code += f"{left} = {expression_table[commutative_rhs]};\n"
                    replaced += 1
                    
                    print(f"value_number_table: {value_number_table}")
                    print("=======================")
                    print(f"expression_table: {expression_table}")
                    print("=======================")
                    print(f"optimized code: ")
                    print(optimized_code)
                    print("=============================================================")
                    continue
                

            # If expression is new, add to tables and output code
            optimized_code += f"{left} = {right};\n"
            
            # right_0 = right
            # operands = right.split(" ")
            # if len(operands) == 3 and operands[1] == "-":
            #     if operands[0] == operands[2]:
            #         zero = "0"
            #         right_0 = zero
            value_number_table[left] = right_0
            # print(f"Added {left} = {right} to value number table")
            keys_to_delete = [key for key, value in expression_table.items() if value == left]
            for key in keys_to_delete:
                del expression_table[key]

            expression_table[right_0] = left
            # print(f"Added {right} = {left} to expression table")
            print(f"value_number_table: {value_number_table}")
            print("=======================")
            print(f"expression_table: {expression_table}")
            print("=======================")
            
            # Update the expression table with the new variable
            
   
                    
                    
            print(f"optimized code: ")
            print(optimized_code)
            print("=============================================================")
                    

        # print(f"value_number_table: {value_number_table}")
        # print("=======================")
        # print(f"expression_table: {expression_table}")
        # print("=======================")
        # print(f"optimized code: {optimized_code}")
        # print("=======================================")
        # print(expression_table)
        # print("=======================")
        
        
    # # Prepare the new variable declarations
    # new_variable_declarations = "\n".join([f"int {var};" for var in new_variables])

    # print(pre)

    # # hint: print out any new variable declarations you need here
    # if new_variable_declarations:
    #     print(new_variable_declarations)
        
    # # hint: print out the optimized local block here
    # print("// Start optimization range")
    # print(optimized_code.strip())
    # print("// End optimization range")
    
    # # hint: store any new numbered variables back to their unumbered counterparts here


    # print(post)
        



    # You should keep track of how many instructions you replaced
    #print("// replaced: " + str(replaced))  
    print(f"// replaced: {replaced}")  
    

# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.
if __name__ == '__main__': 
    parser = argparse.ArgumentParser()   
    parser.add_argument('cppfile', help ='The cpp file to be analyzed') 
    args = parser.parse_args()
    local_value_numbering(args.cppfile)
