# Modify the convert.py program (Section 2.2) with a loop so that it executes 5 times before
# quitting (i.e., it converts 5 temperatures in a row).
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
    print("A Program to convert 5 Celsius temperatures to Fahrenheit successively!")

    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32

        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()