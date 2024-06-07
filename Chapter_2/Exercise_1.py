# A user-friendly program should print an introduction that tells the user what the program does.
# Modify the convert.py program (Section 2.2) to print an introduction.
#       #  convert.py
#       #  A program to convert Celsius temps to Fahrenheit
#       #  by: Susan Computewell
#           def main():
#               celsius = eval(input("What is the Celsius temperature? "))
#               fahrenheit = 9/5 * celsius + 32
#               print("The temperature is", fahrenheit, "degrees Fahrenheit.")
#
#           main()


def main():
    print("A Program to convert Celsius temperature to Fahrenheit")

    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32

    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
