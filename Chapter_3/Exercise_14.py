# Write a program that finds the average of a series of numbers entered by the user. As in the
# previous problem, the program will first ask the user how many numbers there are. Note: the
# average should always be a float, even if the user inputs are all ints.

def main():
    print("A program to find the average of a series of numbers")
    print()
    
    # Numbers to be averaged
    total_numbers = int(input("How many numbers are to be averaged: "))
    
    # Get numbers and the sum of the numbers
    total_sum = 0
    for i in range(total_numbers):
        number = int(input(f"Enter number {i + 1}: "))
        total_sum += number
    
    # Average
    average = total_sum / total_numbers
        
    print(f"The average numbers is {average:.2f}")

main()
