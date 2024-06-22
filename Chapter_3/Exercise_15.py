#  Write a program that approximates the value of π by summing the terms of this series:
#  4/1 − 4/3 + 4/5 − 4/7 + 4/9 − 4/11 + . . . The program should prompt the user for n, the number of
#  terms to sum, and then output the sum of the first n terms of this series. Have your program
#  subtract the approximation from the value of math.pi to see how accurate it is.


import math
def leibniz(n):
    #Calculate the sum of the first n terms of the Leibniz series to approximate π.
    
    series_sum = 0  # Initialize the sum to 0
    # Loop through the first n terms
    for i in range(n):
        if i % 2 == 0:
            series_sum += 4 / ((2 * i) + 1)  # Add the term for even indices
        else:
            series_sum -= 4 / ((2 * i) + 1)  # Subtract the term for odd indices
    return series_sum  # Return the calculated sum

def main():
    print("A program that approximates the value of π (Using Leibniz series)")
    print()

    # Prompt the user for the number of terms
    terms = int(input("Enter the number of terms to sum: "))

    # Calculate the approximation of π using the Leibniz series
    series_sum = leibniz(terms)
    
    # Calculate the difference between the approximation and the actual value of π
    difference = math.pi - series_sum

    print(f"The approximate value of π after summing {terms} terms is {series_sum:.4f}")
    print(f"The actual value of π is {math.pi:.4f}")
    print(f"The difference between the approximation and the actual value is {difference:.4f}")

main()
