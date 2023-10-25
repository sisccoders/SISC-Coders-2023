def main():
    temp_celsius = float(input("Enter temperature in Celsius: "))
    conversion_choice = input("Convert to Fahrenheit or Kelvin (F/K): ")

    converted_temp = convert_temperature(temp_celsius, conversion_choice)
    print(f"Converted temperature: {converted_temp:.2f}")

def convert_temperature(temp_celsius, conversion_choice):
    match conversion_choice:
        case 'F':
            return temp_celsius * 1.8 + 32
        case 'K':
            return temp_celsius + 273.15

if __name__ == '__main__':
    main()