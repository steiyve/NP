# TODO: mudolarize the code for the arithmetics operation
# TODO: implement a line by line mode
# TODO: fix the missing tabs error when checking for syntax


import sys
from arithmetics import add, sub, mul, div
from bio import print_func, input_func

variables: dict[str, any] = {}


def define_var(line: str) -> None:
    """
    This function is used to define variables in the DATA block
    :param line: str
    :retrun: None
    """
    if line == "\n":
        return
    
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
    # if not line.startswith('\t'):                                   # Check if the line start whit a tab
    #     raise SyntaxError("SyntaxError: Missing tabs")
    
    # Format the string to be interpreted
    line = line.removeprefix('\t')

    if line.strip() == '\n':                                        # If the line is empty exit the if statement
        return
    
    # Check if the line is a print statement
    if line.strip().startswith("print"):
        line = line.strip()
        sys.stdout.write('\033[F')                                  # Move the cursor up one line
        sys.stdout.write('\033[K')                                  # Clear the line
        print_func(line, variables)                                 # Call the print function
    
    # Check if the line is an input statement
    if line.strip().startswith("input"):
        input_func(line, variables)                                 # Call the input function



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
                print_func(line, variables)
            
            if line.strip().startswith("input"):                    # Check if the line is an input statement
                input_func(line, variables)

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