def convert_to_letter(percent_grade):
    '''
    Take the percentage and convert it to its corresponding letter grade.
    '''
    if percent_grade > 100:
         print('Invalid')
    else:
        if percent_grade > 95:
            print('VS')
        if percent_grade > 90:
            print('S')
        if percent_grade > 85:
            print('AA')
        if percent_grade >= 80:
            print('A')

convert_to_letter(96)