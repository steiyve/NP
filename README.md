# Custom Language Compiler

This project is a simple **compiler** for a custom language. It supports basic **arithmetic operations**, **variable definitions**, **conditional statements**, and **input/output operations**.

---

## Project Structure

```plaintext
/home/nicolas/language/
├── src/
│   ├── compiler.py
│   ├── print.py
│   ├── input.py
│   └── aritmethics.py
├── add.np
└── README.md
```

## Files Overview

### `compiler.py`
This is the main file that drives the compiler. It reads the input file, processes each line, and executes the corresponding operations.

### `print.py`
Contains the `print_func` function, which handles `print` statements in the custom language.

### `input.py`
Contains the `input_func` function, which handles `input` statements in the custom language.

### `aritmethics.py`
Contains functions for basic arithmetic operations:

- **`add(line: str) -> None`**: Adds two numbers.
- **`sub(line: str) -> None`**: Subtracts two numbers.
- **`mul(line: str) -> None`**: Multiplies two numbers.
- **`div(line: str) -> None`**: Divides two numbers.

### `add.np`
An example input file for the compiler. It contains variable definitions and arithmetic operations.

## Usage

### 1. **Define Variables**
Variables are defined in the `DATA block` section of the input file.

### 2. **Arithmetic Operations**
You can perform the following operations:

- **Addition** (`+`)
- **Subtraction** (`-`)
- **Multiplication** (`*`)
- **Division** (`/`)

### 3. **Conditional Statements**
Use `if` statements to perform conditional operations.

### 4. **Input/Output**
- **`print`**: Outputs data to the console.
- **`input`**: Accepts user input.

### Example Input File (`add.np`)

```plaintext
DATA block:
    b = 1
    c = 2
    a = 0
    d = 3
    f = 0
    z = 34

a = b + c
d = d + 3
f = 3 + 4
z = z - 22
a = 3
```

## Running the Compiler

To run the compiler, use the following command:

```bash
python3 compiler.py add.np
```

## Contributing

Feel free to contribute to this project by submitting **issues** or **pull requests**. Your contributions are always welcome!

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

### Reporting Issues

If you encounter any issues or bugs, please submit an **issue** with detailed information, including:

- Steps to reproduce the issue.
- Expected vs. actual results.
- Any relevant logs or error messages.

Thank you for your contributions!

