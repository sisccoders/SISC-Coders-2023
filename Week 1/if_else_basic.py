def main():
    age = int(input('How old? '))
    print(categorize_age(age))

def categorize_age(age):
    '''
    Categorizes a person's age into groups

    Parameters:
    age - the age of the person

    Returns:
    'Child' for 0-12, 'Teen' for 13-19, 'Adult' for 20-64, and 'Senior' for 65+

    Hint
    use if-else statement
    '''
    if age < 0:
        return("invalid")
    else:
        if age <= 12:
            return("Child")
        elif age <=19:
            return('Teen')
        elif age <=64:
            return("Adult")
        else:
            return('Senior')

main()