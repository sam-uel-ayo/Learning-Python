# Write a program that converts distances measured in kilometers to miles. One kilometer is
# approximately 0.62 miles.

def main():
    print("A Program to convert distance in Kilometers to Miles")
    
    kilometers = eval(input("What is the  distance in Kilometers? "))
    miles = kilometers * 0.62
    
    print("The distance is", miles, "Miles.")
main()   