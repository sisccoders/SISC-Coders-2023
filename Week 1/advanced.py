# Before You Begin

# On the terminal, execute
# $ cd 'Week 1'
# Next
# $ mkdir 'yourname/s'
# $ cd 'yourname/s'
# $ code temp.py (advanced)



# Advanced:
# In various scientific and everyday applications, it's common to convert temperatures between Celsius,
# Fahrenheit, and Kelvin. Whether you're working in a lab or just checking the weather, having a tool for this
# can be handy. Here's a basic framework for a temperature conversion tool:

def main():
    temp_celsius = float(input("Enter temperature in Celsius: "))
    conversion_choice = input("Convert to Fahrenheit or Kelvin (F/K): ")

    converted_temp = convert_temperature(temp_celsius, conversion_choice)
    print(f"Converted temperature: {converted_temp:.2f}")

def convert_temperature(temp_celsius, conversion_choice):
    # TODO

if __name__ == '__main__':
    main()

# We've got the skeleton of a temperature conversion tool here, but there are some gaps to fill in:

# 1. convert_temperature(temp_celsius, conversion_choice):
# This function should accept a float representing a temperature in Celsius and a string representing the
# user's conversion choice ('F' for Fahrenheit, 'K' for Kelvin). It should return the converted temperature
# as a float.
#     If the conversion choice is 'F', how do we convert from Celsius to Fahrenheit?
#     If the conversion choice is 'K', how do we convert from Celsius to Kelvin?

# Assume that the user will input a valid float for the temperature in Celsius, and a valid string ('F' or 'K')
# for the conversion choice.

# How to Test

# Run your program with python temp.py
# Type 25 and press Enter. Then, type F and press Enter. Your program should output:

# Converted temperature: 77.00


# Run your program with python temp_conversion.py.
# Type 0 and press Enter. Then, type K and press Enter. Your program should output:

# Converted temperature: 273.15


# Run your program with python temp_conversion.py.
# Type -40 and press Enter. Then, type F and press Enter. Your program should output:

# Converted temperature: -40.00