from random import randrange

def main():
    x = randrange(1,100,1) #chooses random integer from 1 to 99 and assigns it to x
    guessed = False #sets a variable that contains the state of the game
    guess_count = 0 #counts the number of guesses the user made so far

    while not guessed:
        '''
        Receives guess from user. Tells user if the guess is higher or lower than the number.
        Reminds user to type an integer if the user does not.
        No limit on number of guesses.
        User wins if guesses the correct number.
        '''
        guess_count += 1
        try:
            guess = int(input())
            if guess == x:
                guessed = True
            elif guess < x:
                print('Type a higher number')
            else:
                print('Type a lower number')
        except ValueError:
            print('Please type an integer')

    print(f'Congratulations! You guessed it in {guess_count} tries.')

if __name__ == '__main__':
    main()