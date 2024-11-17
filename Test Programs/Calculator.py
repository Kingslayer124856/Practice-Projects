"""
Project Calculator
Created on: 1/10/2023
Edited 1: 17/11/2024
Made by: Cassandra King 
"""
# find a way to include more than 2 numbers in the calculation

menu = '(+)Addition \n(-)Subtraction \n(x)Multiplication \n(/)Division'

def main():
    """Menu of calculation options """
    print("Please select an option")
    print (menu)
    choice = input("Choice: ").lower()
    if choice == ('+'):
        addition()
    elif choice == ('-'):
        subtraction()
    elif choice == ('x'):
        multipy()
    elif choice == ('/'):
        divide()
    else:
        print("Option not available try again")
        main()

def again():
    """ask user if they would like to use calculator again"""
    print("Would you like to calculate again?")
    usage = input("Y/N: ").upper()
    if usage == ('Y'):
        main()
    elif usage == ('N'):
        print("Thank you for calculating today")
    else:
        print("Incorrect selection \nTry again")
        again()


def addition():
    """Calculating the addition of 2 numbers"""
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    sum = num1 + num2
    print("Sum: ", sum)
    again()


def subtraction():
    """Calculating the subtraction of 2 numbers"""
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    sum = num1 - num2
    print("Sum: ", sum)
    again()

def multipy():
    """Calculating the multiplication of 2 numbers"""
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    sum = num1 * num2
    print("Sum: ", sum)
    again()

def divide():
    """Calculating the division of 2 numbers"""
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    sum = num1 / num2
    print("Sum: ", sum)
    again()

main()