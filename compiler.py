
# TODO: implement a line by line mode
# TODO: fix the missing tabs error when checking for syntax


import sys
from arithmetics import add, sub, mul, div
from bio import print_func, input_func
from line import line_mode
from logic import if_call, execute_if
from loops import for_loop


variables: dict[str, any] = {}


def define_var(line: str) -> None:
    """
    This function is used to define variables in the DATA block
    :param line: str
    :retrun: None
    """
    if line == "\n":
        return
    
    # if '=' not in line:
    #     raise SyntaxError("SyntaxError: Missing equal sign")
    
    try:
        name = line.split('=')[0].removeprefix('\t')                    # Remove tabs from the name
        name = name.strip()                                             # Remove any remaining leading/trailing whitespace
        value = line.split('=')[1].replace('"', '')
        value = value.strip()
    except IndexError:
        return
    variables[name] = value




def main() -> int:
    try:
        filename = sys.argv[1]
    
    except IndexError:
        line_mode()
        return 0


    with open(filename, "r") as f:                                  # Open the file
        skip_next_line = False
        if_skip = False

        # Loop through the file one line at a time
        for line in f:
            if line.strip().startswith("#"):                        # If the line is a comment skip it
                continue
            
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

            if line.startswith("for"):
                for_loop(line, variables)              

    return 0

if __name__ == "__main__":
    main()