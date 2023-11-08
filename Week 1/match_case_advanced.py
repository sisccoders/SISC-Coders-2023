from sys import exit

memory = 0

def main():
    global memory
    while True:
        try:
            memory = int(input("What is the initial number? "))
            break
        except ValueError:
            print('Please type a number')
    while True:
        process_command(input("Command: "))
        print(f'Current memory: {memory}')

def calculate(operation, number=None):
    '''
    Performs arithmetic operations on a global 'memory' variable, updating its value based on the operation specified.

    The function interprets the 'operation' parameter to perform arithmetic on 'memory' using 'number' when provided.
    The 'reset' operation does not require 'number' and resets 'memory' to zero. The function ensures that 'memory' is
    not divided by zero and handles unknown operations by returning an error message.

    Parameters:
    - operation (str): A string representing the arithmetic operation to perform. Valid operations are 'add', 'subtract', 'multiply', 'divide', and 'reset'.
    - number (str): A string representing the numeric value to be used in the operation. This parameter is expected to be convertible to a float. It is not required for the 'reset' operation.

    Returns:
    - str: A string message indicating the result of the operation or an error.
    '''
    global memory
    if number is not None:
        try:
            number = float(number)
        except ValueError:
            return "Error: The number provided is not valid."

    match operation:
        #TODO
        '''
        Specification
        - 'add': Add 'number' to the current value in 'memory'.
        - 'subtract': Subtract 'number' from the current value in 'memory'.
        - 'multiply': Multiply the current value in 'memory' by 'number'.
        - 'divide': Divide the current value in 'memory' by 'number', ensuring not to divide by zero.
        - 'reset': Reset the value of 'memory' to zero. This operation does not require a 'number' parameter.

        For the 'divide' operation, you must ensure that 'number' is not zero to avoid a division by zero error. If 'number' is zero,
        the function should return an error message. For any operation not recognized by the 'match-case' block, the function should
        return an "Error: Unknown operation." message.

        Hints
        - Use the 'match-case' statement to compare 'operation' against the expected operations.
        - Ensure the 'match-case' block is exhaustive, covering all possible valid operations and including a default case for error handling.
        - Remember to update 'memory' directly within each case block where applicable.

        How to Test
        >>> Run python match_case_advanced.py
        >>> Set initial memory to 0
        >>> Command: add 10 #expect console to print 10 out
        >>> Command: subtract 5  # Subtract 5 from memory, expect memory to be 5 if it was 10 before.
        >>> Command: multiply 2  # Multiply memory by 2, expect memory to be 10 if it was 5 before.
        >>> Command: divide  # Attempt to divide by zero, print an error message.
        >>> Command: reset  # Reset memory, expect memory to be 0.
        >>> Command: power  # An example of an invalid operation, print an error message.
        >>> Command: exit #Expect the program to print Goodbye! and terminate

        Relevant Documentation Links:
        - For 'match-case' syntax and usage: https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
        - For understanding global variables in functions: https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-global-and-nonlocal-statements
        - For converting strings to floats and handling exceptions: https://docs.python.org/3/library/stdtypes.html#float

        Note: As the name suggests, this is advanced. Feel free to collaborate with your friends or ask the leaders.
        '''

    return f"Current value: {memory}"

def process_command(command):
    parts = command.split()
    if parts[0] == "reset":
        return calculate("reset")
    elif parts[0] == "exit":
        exit('Goodbye!')
    elif len(parts) == 2:
        operation, number = parts
        return calculate(operation, number)
    else:
        return print("Error: Invalid command format.")

if __name__ == '__main__':
    main()