from compiler import variables
from basic_io import print_func, input_func
import sys

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
    
    operator1 = line[0]                                             # Get the first operator of the condition
    operator2 = line[2].replace('"', '')                            # Get the second operator of the condition  
    operator2 = operator2.replace(':', '')
    operator2 = operator2.strip()
    condition = line[1]                                             # Get the symbol of the condition

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
