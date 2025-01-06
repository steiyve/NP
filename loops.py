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
    start    = int(parts[2])
    end      = int(parts[3])
    step     = int(parts[4].removesuffix(":"))
    code     = parts[5:]
    
    code = ' '.join(code)
    print(code)

    

    if start in variables.keys():
        start = variables[start]
    if end in variables.keys():
        end = variables[end]
    if step in variables.keys():
        step = variables[step]

    return start, end, step, var_name, code
    # TODO: add suport for the arithmetics and logic functions



def execute_for(line: str, variables: dict):
    if line.startswith("print"):
        print_func(line, variables)
    
    if line.startswith("input"):
        input_func(line, variables)
    
    if '+' in line:
        add(line, variables)
    
    if '-' in line:
        sub(line, variables)
    
    if '*' in line:
        mul(line, variables)
    
    if '/' in line:
        div(line, variables)


    