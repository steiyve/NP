def add(line: str, variables: dict) -> None:
    """
    This function is used to add two numbers
    :param line: str
    :return: None
    """
    # Format and split the line
    line = line.removesuffix('\n')
    line = line.strip()
    line = line.split(' ')

    # Check if the line is the good format
    if len(line) != 5:
        raise SyntaxError("SyntaxError: Missing operator")
    
    # Example: line = ['a', '=', 'b', '+', 'c']    
    if line[2] in variables.keys():                             # Check if the variable is in the variables dictionary
        line[2] = variables[line[2]]                            # Replace the variable with its value

    if line[4] in variables.keys():                             # Check if the variable is in the variables dictionary
        line[4] = variables[line[4]]                            # Replace the variable with its value
    
    variables[line[0]] = float(line[2]) + float(line[4])        # Add the two numbers and store the result in the variables dictionary

    

def sub(line: str, variables: dict) -> None:
    """
    This function is used to subtract two numbers
    go see the add function for more information on how this function works
    :param line: str
    :return: None
    """
    
    line = line.removesuffix('\n')
    line = line.strip()
    line = line.split(' ')

    # Check if the line is the good format
    if len(line) != 5:
        raise SyntaxError("SyntaxError: Missing operator")
    
    # Example: line = ['a', '=', 'b', '+', 'c']    
    if line[2] in variables.keys():
        line[2] = variables[line[2]]

    if line[4] in variables.keys():
        line[4] = variables[line[4]]
    
    variables[line[0]] = float(line[2]) - float(line[4])

def mul(line: str, variables: dict) -> None:
    """
    This function is used to multiply two numbers
    go see the add function for more information on how this function works
    :param line: str
    :return: None
    """
    line = line.removesuffix('\n')
    line = line.strip()
    line = line.split(' ')

    # Check if the line is the good format
    if len(line) != 5:
        raise SyntaxError("SyntaxError: Missing operator")
    
    # Example: line = ['a', '=', 'b', '+', 'c']    
    if '=' in line:
        if line[2] in variables.keys():
            line[2] = variables[line[2]]

        if line[4] in variables.keys():
            line[4] = variables[line[4]]
        
        variables[line[0]] = float(line[2]) * float(line[4])
    
    else: 
        print(float(line[2]) * float(line[4]))
    
def div(line: str, variables) -> None:
    """
    This function is used to divide two numbers
    go see the add function for more information on how this function works
    :param line: str
    :return: None
    """
    line = line.removesuffix('\n')
    line = line.strip()
    line = line.split(' ')

    # Check if the line is the good format
    if len(line) != 5:
        raise SyntaxError("SyntaxError: Missing operator")
    
    # Example: line = ['a', '=', 'b', '+', 'c']    
    if line[2] in variables.keys():
        line[2] = variables[line[2]]

    if line[4] in variables.keys():
        line[4] = variables[line[4]]
    
    variables[line[0]] = float(line[2]) / float(line[4])
    
