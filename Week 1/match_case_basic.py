def main():
    c = input("What's the color of the traffic light? ") #Asks for color of the traffic light
    print(traffic_light_action(c))

def traffic_light_action(color: str):
    #TODO
    '''
    Implement a function that returns different strings depending on the color of the traffic light
    Fix extra spaces or wrong capitalizations
        '    red' and ' rEd' is equal to 'red'

    Parameters:
    color - the current color of the traffic light

    Returns:
    a string that says
        'Go' when the color is green
        'Slow down' when the color is yellow
        'Stop' when the color is red
        'Invalid color' when it isn't any of the three

    How to Test
    Run python match_case_basic.py and type red when prompted question. The function should return 'Stop'
    Run python mmatch_case_basic.py and type     red when prompted question. The function should return 'Stop'
    Run python match_case_basic.py and type gReEn when prompted question. The function should return 'Go'
    Run python match_case_basic.py and type yell0w when prompted question. The function should return 'Invalid color'
    '''

main()