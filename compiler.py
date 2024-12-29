# TODO: mudolarize the code for the arithmetics operation
# TODO: implement a line by line mode


import sys
from arithmetics import add, sub, mul, div


variables: dict[str, any] = {}


def print_func(line: str) -> None:
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
            str_2_print[pos] = variables[i]                         # Replace the variable with its value
        
    
    # Format the string to be printed
    str_2_print = ' '.join(str_2_print)
    str_2_print = str_2_print.removeprefix("print(")                # Remove the print function symbol
    str_2_print = str_2_print.replace(')', '')                      # Remove the closing bracket
    str_2_print = str_2_print.replace('"', '')                      # Remove the quotes
    str_2_print = str_2_print.strip()

    print(str_2_print)

def input_func(line: str) -> None:
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

def define_var(line: str) -> None:
    """
    This function is used to define variables in the DATA block
    :param line: str
    :retrun: None
    """
    if line == "\n":
        return
    if not line.startswith((' ', '\t')):
        raise SyntaxError("SyntaxError: Missing tabs")
    
    if '=' not in line:
        raise SyntaxError("SyntaxError: Missing equal sign")
    

    name = line.split('=')[0].removeprefix('\t')                    # Remove tabs from the name
    name = name.strip()                                             # Remove any remaining leading/trailing whitespace
    value = line.split('=')[1].replace('"', '')
    value = value.strip()

    variables[name] = value

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

def execute_if(line: str) -> None:
    """
    This function is used to execute the code in the if statement
    :param line: str
    :return: None
    """
    if not line.startswith('\t'):                                   # Check if the line start whit a tab
        raise SyntaxError("SyntaxError: Missing tabs")
    
    # Format the string to be interpreted
    line = line.removeprefix('\t')

    if line.strip() == '\n':                                        # If the line is empty exit the if statement
        return
    
    # Check if the line is a print statement
    if line.strip().startswith("print"):
        line = line.strip()
        sys.stdout.write('\033[F')                                  # Move the cursor up one line
        sys.stdout.write('\033[K')                                  # Clear the line
        print_func(line)                                            # Call the print function
    
    # Check if the line is an input statement
    if line.strip().startswith("input"):
        input_func(line)                                            # Call the input function


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
    if '=' in line:
        if line[2] in variables.keys():
            line[2] = variables[line[2]]

        if line[4] in variables.keys():
            line[4] = variables[line[4]]
        
        variables[line[0]] = float(line[2]) / float(line[4])
    
    else: 
        print(float(line[2]) * float(line[4]))

def main() -> int:
    try:
        filename = sys.argv[1]
    
    except IndexError:
        line_mode = True


    with open(filename, "r") as f:                                  # Open the file
        skip_next_line = False
        if_skip = False

        # Loop through the file one line at a time
        for line in f:
            if skip_next_line == True:                              # If the line is in the DATA block skip it
                define_var(line)

            if line.strip() == "DATA block:":                       # Check if the line is the DATA block
                skip_next_line = True
            
            if line.strip() == "\n":                                # If the line is empty it mean the end of a if statement or the DATA block                          
                skip_next_line = False
                if_skip = False
            
            if line.strip() == "debug":                             # Print the variables dictionary             
                skip_next_line = False
                print(variables)

            if line.strip().startswith("print"):                    # Check if the line is a print statement
                print_func(line)
            
            if line.strip().startswith("input"):                    # Check if the line is an input statement
                input_func(line)

            if line.strip().startswith("if"):                       # Check if the line is an if statement     
                if_skip = if_call(line)
                
            if if_skip == True:                                     # Run the code in the if statement
                execute_if(line)

            # Arithmetic operations
            if '+' in line:
                add(line, variables)

            if '-' in line:
                sub(line, variables)

            if '*' in line:
                mul(line, variables)

            if '/' in line:
                div(line, variables)              

    return 0

if __name__ == "__main__":
    main()