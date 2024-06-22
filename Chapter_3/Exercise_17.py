# Write a program that implements Newton’s method. The program should prompt the user
# for the value to find the square root of (x) and the number of times to improve the guess.
# Starting with a guess value of x/2, your program should loop the specified number of times
# applying Newton’s method and report the final value of guess. You should also subtract your
# estimate from the value of math.sqrt(x) to show how close it is.

import math
def guess_root(x, times):
    # Start with an initial guess value of x/2
    guess = x / 2
    
    # Apply Newton's method times number of times
    for i in range(times):
        guess = (guess + (x / guess)) / 2
    return guess

def main():
    print("A program that implements Newton's method to find square root")
    print()
    
    # Prompt the user for the number to find the square root of
    number = int(input("Enter the value to guess the square root of: "))
    # Prompt the user for the number of iterations to improve the guess
    times = int(input("Enter the number of times to improve the guess: "))
    print()
    
    # Calculate the guessed root using the guess root function
    guessed_root = guess_root(number, times)
    # Calculate the difference between the guessed root and the actual square root
    difference = math.sqrt(number) - guessed_root
    print()
    
    # Display the results
    print(f"The guessed root of {number} after guessing {times} times is {guessed_root:.4f}")
    print(f"The actual square root is {math.sqrt(number):.4f}")
    print(f"The difference between the guessed root and the actual square root is {difference:.4f}")

main()
