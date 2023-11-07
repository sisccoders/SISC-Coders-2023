memory = 0

def calculate(operation, number=None):
    global memory
    if number is not None:
        try:
            number = float(number)
        except ValueError:
            return "Error: The number provided is not valid."

    match operation:
        #TODO
        '''
        '''

    return f"Current value: {memory}"

def process_command(command):
    parts = command.split()
    if parts[0] == "reset":
        return calculate("reset")
    elif len(parts) == 2:
        operation, number = parts
        return calculate(operation, number)
    else:
        return "Error: Invalid command format."