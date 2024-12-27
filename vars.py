from compiler import variables

def define_var(line: str) -> None:
    """
    This function is used to define variables in the DATA block
    :param line: str
    :retrun: None
    """
    if line == "\n":
        return
    if not line.startswith((' ', '\t')):
        return
    

    name = line.split('=')[0].removeprefix('\t')                    # Remove tabs from the name
    name = name.strip()                                             # Remove any remaining leading/trailing whitespace
    value = line.split('=')[1].replace('"', '')
    value = value.strip()

    variables[name] = value
