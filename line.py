import sys
from arithmetics import add, sub, mul, div
from bio import print_func, input_func

variables: dict = {}

def if_call(line: str) -> bool:
    """
    This function is used to call the if statement
    :param line: str
    :return: bool
    """

    # Format the string to be interpreted
    line = line.removeprefix("if")                                  # Remove the if statement                      
    line = line.split(" ")
    del line[0]
    
    try:
        operator1 = line[0]                                             # Get the first operator of the condition
        operator2 = line[2].replace('"', '')                            # Get the second operator of the condition  
        operator2 = operator2.replace(':', '')
        operator2 = operator2.strip()
        condition = line[1]                                             # Get the symbol of the condition
    except IndexError:                                                  # If there is missing condition or symbol                                             
        raise SyntaxError("SyntaxError: Missing condition or symbol")


    # Check if the operator is a variable
    if operator1 in variables.keys():
        operator1 = variables[operator1]                            # Replace the variable with its value
    
    if operator2 in variables.keys():
        operator2 = variables[operator2]                            # Replace the variable with its value

    # Check if the condition is true
    if condition == "==":
        return operator1 == operator2
    
    if condition == "!=":
        return operator1 != operator2

    if condition == "<":
        return operator1 < operator2
    
    if condition == ">":
        return operator1 > operator2

    if condition == "<=":
        return operator1 <= operator2


def line_mode() -> None:
    """
    this function is used to be the line to line mode
    :return: None
    """
    while True:
        line = input(">>> ")
        if line == "exit":
            break
        
        elif line.startswith("if"):
            print(if_call(line))

        elif line.startswith("print("):
            print_func(line, variables)
        
        elif line.startswith("input("):
            input_func(line, variables)
        
        elif line.strip() == "debug":
            print(variables)
        
        elif '+' in line and '=' in line:
            add(line, variables)
        
        elif '-' in line and '=' in line:
            add(line, variables)
        
        elif '*' in line and '=' in line:
            add(line, variables)
        
        elif '/' in line and '=' in line:
            add(line, variables)

        elif '=' in line:
            line = line.split('=')
            variables[line[0].strip()] = line[1].strip()
        
        
        