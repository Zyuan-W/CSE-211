# declare, assign, if, else, for, while, etc.



def parse_cpp_to_ir(cpp_code):
    ir = []
    lines = cpp_code.split('\n')
    for line in lines:
        
        
        # Checking for 'for' loop first due to highest precedence
        if 'for' in line:
            # Simplified parsing for 'for' loop
            parts = line[line.find('(')+1:line.find(')')].split(';')
            if len(parts) == 3:
                init = parts[0].strip()
                p = init.split('=')
                iter = p[0].strip()
                start = p[1].strip()
                condition = parts[1].strip()
                p1 = condition.split('<')
                end = p1[1].strip()
                update = parts[2].strip()
                ir.append(('for', iter, start, end, update))
            continue

        # Checking for 'if' statement next
        if 'if' in line:
            condition = line[line.find('(')+1:line.find(')')]
            ir.append(('if', condition))
            continue
        
        if 'else' in line:
            ir.append(('else',))
            continue

        # Checking for variable declaration and assignment last, as they have equal and lowest precedence
        if 'int ' in line or '=' in line:
            if 'int ' in line:  # Variable declaration
                var_name = line.split()[1].rstrip(';')
                ir.append(('declare', var_name))
            elif '=' in line:  # Assignment
                var_name, value = line.split('=')
                var_name, value = var_name.strip(), value.strip().rstrip(';')
                ir.append(('assign', var_name, value))
            continue

        # Add more parsing logic here for 'else', 'while', etc.

    return ir

        
        
        # if 'int ' in line:  # Variable declaration
        #     var_name = line.split()[1].strip(';')
        #     ir.append(('declare', var_name))
        #     if '=' in line:
        #         var_name, value = line.split('=')
        #         var_name, value = var_name.strip(), value.strip().strip(';')
        #         ir.append(('assign', var_name, value))
        # elif '=' in line:  # Assignment
        #     var_name, value = line.split('=')
        #     var_name, value = var_name.strip(), value.strip().strip(';')
        #     ir.append(('assign', var_name, value))
        # # Add more parsing logic here for if-else, while, for loops, etc.
        # elif 'if' in line:  # If statement
        #     condition = line[line.find('(')+1:line.find(')')]
        #     ir.append(('if', condition))
        # elif 'else' in line:  # Else statement
        #     ir.append(('else',))
        # elif 'for' in line:  # For loop
        #     # Simplified parsing, assumes format: for (init; condition; update)
        #     parts = line[line.find('(')+1:line.find(')')].split(';')
        #     if len(parts) == 3:
        #         init = parts[0].strip()
        #         condition = parts[1].strip()
        #         update = parts[2].strip()
        #         ir.append(('for', init, condition, update))
        # More parsing logic here for while, etc. 
    # return ir

def generate_python_code(ir):
    python_code = ""
    for command in ir:
        if command[0] == 'declare':
            python_code += f"{command[1]} = None\n"
        elif command[0] == 'assign':
            python_code += f"{command[1]} = {command[2]}\n"
        elif command[0] == 'if':
            python_code += f"if {command[1]}:\n"
        elif command[0] == 'else':
            python_code += "else:\n"
        elif command[0] == 'for':
            # init = command[1].replace('int ', '')  # Assuming simple int declaration
            # condition = command[2].replace('>', ' in range(').replace(')', ')')  # Simplified conversion
            # python_code += f"for {init} {condition}:\n"
            # update = command[3]  # Not used in this simple version
            python_code += f"for {command[1]} in range({command[2]}, {command[3]}):\n"
        # Add more logic here for other constructs
    return python_code

# Example C++ Code
cpp_code = """
int x = 5;
int x;  // Variable declaration
if (x < 10) {
    x = 20;
} else {
    x = 10;
}

int a;
for (int i = 0; i < 5; i++) {
    a = i;
}
"""

# Translate to IR
ir = parse_cpp_to_ir(cpp_code)
for command in ir:
    print(command)

# Generate Python Code
python_code = generate_python_code(ir)
print("=====================================")
print("Python Code:")
print(python_code)
