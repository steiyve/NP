from compiler import variables

def print_func(line: str) -> None:
    """
    This function is used to print the output of the print function
    :param line: str
    :return: None
    """
    str_2_print = line.split(',')                                   # Split the line by commas      

    for i in str_2_print:
        if i in variables:                                          # If the variable is in the variables dictionary 
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

    # Format the string to be printed
    line = line.removeprefix("input(")
    line = line.removesuffix(')')

    # Split the line by commas
    str_2_input = line.split(',')


    str_2_input[0] = str_2_input[0].replace('"', '')                # Remove the quotes
    str_2_input[1] = str_2_input[1].removeprefix(" ")
    str_2_input[1] = str_2_input[1].removesuffix(")\n")             # Remove the closing bracket and newline character

    # Get the input from the user
    variables[str_2_input[1]] = input(str_2_input[0])