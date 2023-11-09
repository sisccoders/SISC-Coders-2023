def main():
    name = ask_name()
    print(hello(name))

def hello(name):
    '''
    Prints Hello followed by the name of a person.

    Parameters:
    - name (str): A string representing the name of the person.

    Returns:
    - str: A string message containing Hello name.
    '''
    return f'Hello {name}'

def ask_name():
    '''
    Asks user for their name.

    Returns:
    - str: The input of the user.
    '''
    return input('What is your name? ')

main()