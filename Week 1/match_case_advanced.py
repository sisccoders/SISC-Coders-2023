memory = 0

def calculate(operation, number=None):
    global memory
    if number is not None:
        try:
            number = float(number)
        except ValueError:
            return "Error: The number provided is not valid."

    match operation:
        case "add":
            memory += number
        case "subtract":
            memory -= number
        case "multiply":
            memory *= number
        case "divide":
            if number == 0:
                return "Error: Cannot divide by zero."
            memory /= number
        case "reset":
            memory = 0
        case _:
            return "Error: Unknown operation."

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