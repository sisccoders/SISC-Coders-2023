def convert_to_letter(percent_grade):
    '''
    Take the percentage and convert it to its corresponding letter grade.
    '''
    if percent_grade > 100:
         print('Invalid')
    else:
        [if percent_grade > 95:
            print('VS')
        elif percent_grade > 90:
            print('S')
        elif percent_grade > 85:
            print('AA')
        elif percent_grade >= 80:
            print('A')]

convert_to_letter(96)