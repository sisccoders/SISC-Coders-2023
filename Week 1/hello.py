def main():
    name = receive_input()
    hello(name)

def receive_input():
    name = input('What is your name? ')
    return name

def hello():
    '''
    Asks for the user's name and prints it in terminal
    '''
    print(f'Hello {name}')

main()