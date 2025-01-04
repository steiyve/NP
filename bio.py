# bio stands for Basic Input Output

def print_func(line: str, variables: dict) -> None:
    """
    This function is used to print the output of the print function
    :param line: str
    :return: None
    """
    line = line.strip()
    
    # Check the syntax of the print statement
    if not line.startswith("print(") and not line.endswith(')\n'):
        raise SyntaxError("SyntaxError: Missing parentheses")
    
    str_2_print = line.split(',')                                   # Split the line by commas 
    str_2_print[-1] = str_2_print[-1].removesuffix(')\n')           # Remove the closing bracket and newline character
    
    for i in str_2_print:
        i = i.strip()                                               
        if i in variables.keys():                                   # If the variable is in the variables dictionary 
            pos = str_2_print.index(i)
            str_2_print[pos] = str(variables[i])                    # Replace the variable with its value
        
    
    # Format the string to be printed
    str_2_print = ' '.join(str_2_print)
    str_2_print = str_2_print.removeprefix("print(")                # Remove the print function symbol
    str_2_print = str_2_print.replace(')', '')                      # Remove the closing bracket
    str_2_print = str_2_print.replace('"', '')                      # Remove the quotes
    str_2_print = str_2_print.strip()

    print(str_2_print)

def input_func(line: str, variables: dict) -> None:
    """
    This function is used to take input from the user
    :param line: str
    :return: None
    """
    line = line.strip()

    # Check the syntax of the inout statement
    if not line.startswith("input(") and not line.endswith(')\n'):
        raise SyntaxError("SyntaxError: Missing parentheses")

    # Format the string to be printed
    line = line.removeprefix("input(")
    line = line.removesuffix(')')

    # Split the line by commas
    str_2_input = line.split(',')

    # Check the syntax of the input statement
    if not (str_2_input[0].startswith('"') and str_2_input[0].endswith('"')):
        raise SyntaxError("SyntaxError: Missing quotes")


    str_2_input[0] = str_2_input[0].replace('"', '')                # Remove the quotes
    str_2_input[1] = str_2_input[1].removeprefix(" ")
    str_2_input[1] = str_2_input[1].removesuffix(")\n")             # Remove the closing bracket and newline character

    # Get the input from the user
    variables[str_2_input[1]] = input(str_2_input[0])