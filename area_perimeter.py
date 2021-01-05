#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program finds area and perimeter


def area(length, width):
    # Function calculates area and prints it

    # Process and output
    area = length * width
    print("The area is: {}cm²".format(area))


def perimeter(length, width):
    # Function calculates perimeter and prints it

    # Process and output
    perimeter = 2 * (length + width)
    print("The perimeter is: {}cm".format(perimeter))


def main():
    # Takes user input, passes it to functions and calls them

    print("Give me measurements and I will give you the area and perimeter")

    # Input
    while True:
        # Input
        length_string = input("Enter length (cm): ")

        # Process
        try:
            length = int(length_string)
            assert length > 0
            break
        except AssertionError:
            # Output
            print("This isn't a valid input")
        except Exception:
            # Output
            print("This isn't a valid input")
    # Input
    while True:
        # Input
        width_string = input("Enter width (cm): ")

        # Process
        try:
            width = int(width_string)
            assert width > 0
            break
        except AssertionError:
            # Output
            print("This isn't a valid input")
        except Exception:
            # Output
            print("This isn't a valid input")

    # Calls functions
    area(length, width)
    perimeter(length, width)


if __name__ == "__main__":
    main()
