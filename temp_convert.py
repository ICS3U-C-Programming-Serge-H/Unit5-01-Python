#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: Mar 28, 2025
# This program will ask the user to enter a temperature


def fahrenheit():
    try:
        Celsius = float(input("Enter a temperature in Celsius:"))
        fahrenheit = (9 / 5) * Celsius + 32
        print(
            f"{Celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit."
        )
    except ValueError:
        print("Please enter a valid number")


def main():

    return fahrenheit


fahrenheit()

if __name__ == "__main__":
    main()
