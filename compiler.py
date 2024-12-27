


import sys
from basic_io import print_func, input_func
from vars import define_var
from logics import if_call, execute_if
from aritmethics import add, sub, mul, div

variables: dict[str, any] = {}

def main() -> int:
    filename = sys.argv[1]

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
                add(line)

            if '-' in line:
                sub(line)

            if '*' in line:
                mul(line)

            if '/' in line:
                div(line)              

    return 0

if __name__ == "__main__":
    main()