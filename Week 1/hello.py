def main():
    percent_grade = float(input("What's your grade? "))
    letter_grade = convert_to_letter(percent_grade)
    print(letter_grade)

def convert_to_letter(grade):
    '''
    Converts percent grade to letter grade

    Parameters:
    - grade: The numeric grade of the person.

    Returns:
    - str: The converted letter grade.
    '''

main()