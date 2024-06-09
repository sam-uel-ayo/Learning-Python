# Write a program that converts temperatures from Fahrenheit to Celsius.

def main():
    print("A Program to convert Fahrenheit temperature to Celsius")

    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5/9

    print("The temperature is", celsius, "degrees Celsius.")

main()