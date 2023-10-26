# Before You Begin

# On the terminal, execute
# $ cd 'Week 1'
# Next
# $ mkdir 'yourname/s'
# $ cd 'yourname/s'
# $ code area.py (basic)




# Basic:
# In basic geometry, the area of a rectangle is calculated by multiplying its length by its width. Below is a
# skeleton code for a simple program that takes the dimensions of a rectangle from the user and calculates its
# area.

def main():
    length = length_to_float(input("Enter the length of the rectangle: "))
    width = width_to_float(input("Enter the width of the rectangle: "))
    area = calculate_area(length, width)
    print(f"The area of the rectangle is {area:.2f}")

def length_to_float(l):
    # TODO

def width_to_float(w):
    # TODO

def calculate_area(length, width):
    # TODO

main()

# We've drafted most of the program for you, but three functions need to be completed:

# 1. length_to_float(l):
# This function should accept a string l as input (formatted as ##.##, wherein each # is a decimal digit), and
# return the length as a float. For instance, given '5.00' as input, it should return 5.0.

# 2. width_to_float(w):
# Similar to length_to_float, this function should accept a string w as input (formatted as ##.##), and return
# the width as a float. For instance, given '3.50' as input, it should return 3.5.


# 3. calculate_area(length, width):
# This function should accept two floats representing the length and width of the rectangle, and return the area
# of the rectangle as a float.

# Assume that the user will input values in the expected formats.

# How to Test

# Run your program with python area.py.
# Type 5.00 and press Enter. Then, type 3.00 and press Enter. Your program should output:

# The area of the rectangle is 15.00


# Run your program with python area_calc.py.
# Type 10.00 and press Enter. Then, type 2.00 and press Enter. Your program should output:

# The area of the rectangle is 20.00


# Run your program with python area_calc.py.
# Type 7.50 and press Enter. Then, type 4.00 and press Enter. Your program should output:

# The area of the rectangle is 30.00