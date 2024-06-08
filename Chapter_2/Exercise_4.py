# Modify the convert.py program (Section 2.2) so that it computes and prints a table of Celsius
# temperatures and the Fahrenheit equivalents every 10 degrees from 0C to 100C.
#
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
    print("A program that prints a table of Celsius temperatures ")
    print("and the Fahrenheit equivalents every 10 degrees from 0C to 100C")
    
    print("Temperature  Celsius   Fahrenheit")
    print("---------------------------------")
    
    for celsius in range(0, 101, 10):
        fahrenheit = 9/5 * celsius + 32
        print("              ", celsius, "      ",   fahrenheit)
    
main()