def main():
    today = input('Weather: ').split() #Prompts user for weather today
    if len(today) == 2:
        weather, temperature = today
        print(suggest_activity(weather, temperature))
    else:
        print(suggest_activity(today[0]))
    return

def suggest_activity(weather, temperature=None):
    """
    Suggests an activity based on the current weather conditions and temperature.

    Specification:
    - The function provides activity suggestions considering the 'weather' condition as a primary factor.
    - Weather conditions are handled as lowercase strings to ensure case-insensitive matching.
    - The function returns a suggestion string or an error message if the input is invalid.
    - You may assume that the user won't type in decimals for temperature

    Hints:
    - Convert the 'weather' parameter to lowercase to perform case-insensitive comparison.
    - Convert the 'temperature' parameter to integer to perform arithmetic comparisons
    - Use `isdigit()` to verify that 'temperature' is a numeric string before converting to an integer.
    - Provide default activity suggestions for unspecified weather conditions to handle unexpected or unknown inputs.
    - Use descriptive messages for suggestions to enhance user interaction with the program.

    How to Test:

    Run the file by typing python if_else_advanced.py in the terminal

    1. Test with sunny weather and high temperature:
   >>> Weather: Sunny 35
   >>> Expected Output: "It's a great day for swimming or enjoying a cold drink by the beach!"

    2. Test with sunny weather and moderate temperature:
   >>> Weather: Sunny 20
   >>> Expected Output: "Perfect weather for a picnic or a hike in the nature park."

    3. Test with rainy weather without temperature:
   >>> Weather: Rainy
   >>> Expected Output: "A rainy day is perfect for visiting a museum, reading a book, or enjoying a coffee at a cozy cafe."

    4. Test with snowy weather and sub-zero temperature:
   >>> Weather: Snowy -5
   >>> Expected Output: "Bundle up for some snowboarding or build a snowman outside!"

    5. Test with cloudy weather:
   >>> Weather: Cloudy
   >>> Expected Output: "Cloudy days are great for photography or a leisurely walk in the park."

    6. Test with windy weather:
   >>> Weather: Windy
   >>> Expected Output: "Windy conditions are ideal for flying a kite or windsurfing if you're near water."

    7. Test with an unknown weather condition:
   >>> Weather: Foggy
   >>> Expected Output: "Weather condition unknown. Why not plan an indoor activity just to be safe?"

    8. Test with invalid temperature input (non-numeric):
   >>> Weather: Sunny hot
   >>> Expected Output: "Invalid temperature input. Please provide an integer value for temperature."

    9. Test with sunny weather and edge-case temperature (boundary testing):
   >>> Weather: Sunny 30
   >>> Expected Output: "Perfect weather for a picnic or a hike in the nature park."

    10. Test with case insensitivity for weather input:
    >>> Weather: sUnNy 30
    >>> Expected Output: "Perfect weather for a picnic or a hike in the nature park."

    11. Test with missing temperature for weather conditions that provide optional temperature-based suggestions:
    >>> Weather: Sunny
    >>> Expected Output: "Perfect weather for a picnic or a hike in the nature park."

    12. Test with extreme temperatures to check additional advice:
    >>> Weather: Sunny 40
    >>> Expected Output: "It's really hot outside. Stay hydrated and avoid strenuous outdoor activities."

    >>> Weather: Snowy -20
    >>> Expected Output: "It's quite cold. Dress warmly and consider indoor activities unless you enjoy the chill."

    Relevant Documentation Links:
    - For string methods like `lower()` and `isdigit()`: https://docs.python.org/3/library/stdtypes.html#string-methods
    - For information on optional and keyword parameters in functions: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
    - For general error handling in Python: https://docs.python.org/3/tutorial/errors.html
    - For int() function usage and exceptions: Python 3 documentation for int

    Note: As the name suggests, this is advanced. Feel free to collaborate with your friends or ask the leaders.
    """
    #TODO


if __name__ == '__main__':
    main()