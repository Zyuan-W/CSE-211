## tasks

# 1. parser for c++
    develop a basic version of the parser capable of handling simple c++ constructs

```
def parse_cpp_to_ir(cpp_code):
    return ir

```


['func_declare', 'addNumbers', [['int', 'a'], ['int', 'b']], 'int']



['declare', 1, 'x', 10]
['declare', 1, 'y', 20]
['assign', 1, 'y', 'x + y']



['while', 1, 'j >= 0']
('left_brace', '{')
['cout', 2, [['j'], ['" "']]]
['update', 2, 'j', '-=', 1]
('right_brace', '}')
['cout', 1, [['endl']]]




````
ir: ir[0] = command, ir[1] = scopes

    declare: ('declare', var_name, value)

    assignment: ('assign', var_name, value)

    function: ('function', function_name, parameters, return_type)

    func_declare: ('func_declare', name, args, return_type) 

    func_call: ('func_call', function_name, args_list)

    func_call_assign: ('func_call_assign', var, function_call)

    if: ('if', condition)

    else: ('else')

    for: ('for', iter, start, end, update)

    while: ('while', condition)

    cout: ('cout', content)

    return: ('return', expr)

    {: ('left_brace', '{')

    }: ('right_brace', '}')
    

    


````  


```
rule for intermediate representation:

variable declaration: ('declare', var_name, value)
int x = 10;  ==> ('declare', 'x', '10')
int y; ==> ('declare', 'y','0')

variable assignment: ('assign', var_name, value)
x = 11; ==> ('assign', 'x', '11')

if statement: ('if', condition)
if (sum = 10); ==> ('if', 'sum = 10')

For loop: ('for', iter, start, end, update)
for (int i = 0; i < 5; i++) ==> ('for', 'int i', '0', '5', 'i+1')

while loop: ('while', condition)
while (j = 5) ==> ('while', 'j = 5')


```


# 2. Python Code Generation module

# Convert the interpreted IR into Python code

```

check the spacing

check the grammar

check the data type

data structure

```



# 3. Optimization module

# To optimize the generated Python code

```
optimize when generate the python code

parallel for loops as example

    detect the parallel for loop

    use the scope to store the content in blocks

    when parsing for loop, mark it as need to optimize

    def for_optimize(blocks)


```


# 4. Initial Testing and Debugging for the translator


# 5. Report


