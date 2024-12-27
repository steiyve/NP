# TODO: clear up the code
# TODO: implement simple arithmetics

import sys
import re

class Compiler:
    def __init__(self):
        self.variables = {}

    def define_var(self, line: str) -> None:
        if line == "\n" or not line.startswith((' ', '\t')):
            return

        name, value = map(str.strip, line.split('='))
        name = name.removeprefix('\t')
        value = value.replace('"', '')

        self.variables[name] = value

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def evaluate_condition(self, line: str) -> bool:
        line = line.removeprefix("if").split(" ")
        del line[0]

        operator1, condition, operator2 = line[0], line[1], line[2].replace('"', '').replace(':', '').strip()

        operator1 = self.variables.get(operator1, operator1)
        operator2 = self.variables.get(operator2, operator2)

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

    def execute_if(self, line: str) -> None:
        line = line.removeprefix('\t').strip()
        if line == '\n':
            return

        if line.startswith("print"):
            self.remove_last_line()
            self.print_func(line)
        elif line.startswith("input"):
            self.input_func(line)

    def remove_last_line(self):
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')

    def print_func(self, line: str):
        # Implement the print function logic here
        pass

    def input_func(self, line: str):
        # Implement the input function logic here
        pass

def main() -> int:
    compiler = Compiler()
    filename = sys.argv[1]
    with open(filename, "r") as file:
        for line in file:
            compiler.define_var(line)
            if line.startswith("if"):
                if compiler.evaluate_condition(line):
                    next_line = file.readline()
                    compiler.execute_if(next_line)
    return 0

if __name__ == "__main__":
    sys.exit(main())