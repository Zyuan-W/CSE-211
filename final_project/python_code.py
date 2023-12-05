flag = 0
    
    
def function():
    global flag
    flag += 1
        


def function_0():
    global flag
    function()
    flag += 2
    
function_0()
print(flag) # flag is 3 here
    



