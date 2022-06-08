#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import constants


def main():
    # I am the main function
    counter = 0
    sum = 0

    # input
    str_number = input("How many number do you want to add: ")

    # process & output
    try:
        int_number = int(str_number)
        for counter in range(int_number):
            num = float(input("number: "))
            counter = counter + 1
            if num > 0:
                sum += num
            else:
                continue
        print("Sum of positive numbers is {}.".format(sum))
    except Exception:
        print("Invalid Input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
