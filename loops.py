import sys
from arithmetics import add, sub, mul, div
from bio import print_func, input_func
from logic import if_call, execute_if

def for_loop(line, variables):
    """
    This function is called when the line is a for loop statement.
    """
    # Example: for i in 0 10 1: 
    line = line.strip()
    line = line.removeprefix("for ")
    line = line.removesuffix("\n")
    parts = line.split(' ')
    
    print(parts)
    
    
    var_name = parts[0]
    start    = parts[2]
    end      = parts[3]
    step     = parts[4].removesuffix(":")
    code     = parts[5]
    

    if start in variables.keys():
        start = variables[start]
    if end in variables.keys():
        end = variables[end]
    if step in variables.keys():
        step = variables[step]

    for i in range(int(start), int(end), int(step)):
        variables[var_name] = i
        if code.startswith("print"):
            print_func(code, variables)
        
        if code.startswith("input"):
            input_func(code, variables)
        
    # TODOL: add suport for the arithmetics and logic functions


    return 0