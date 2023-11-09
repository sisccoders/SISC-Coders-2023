def main():
    numeric_grade = float(input("What's your grade? "))
    letter_grade = convert_to_letter(numeric_grade)
    print(letter_grade)

def convert_to_letter(grade):
    '''
    Converts numeric grade to letter grade

    Parameters:
    - grade: The numeric grade of the person.

    Returns:
    - str: The converted letter grade.
    '''
    if grade <= 100:
        if grade > 95:
            return 'VS'
        elif grade > 90:
            return 'S'
        elif grade > 85:
            return 'AA'
        elif grade >= 80:
            return 'A'
        elif grade >= 70:
            return 'LA'
        elif grade >= 0 and grade < 70:
            return 'P'
    else:
        return 'Please type a valid grade (0-100).'

main()