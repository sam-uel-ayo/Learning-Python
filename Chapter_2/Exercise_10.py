# Write a program to perform a unit conversion of your own choosing. Make sure that the
# program prints an introduction that explains what it does.

def main():
    print("A Program to convert weight from Pounds to Kilograms")
    
    pounds = eval(input("What is the weight in Pounds?: "))
    kilograms = pounds * 0.453592
    
    print("The weight is", kilograms, "Kilograms.")
main()
