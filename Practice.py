def main():
    print("A program to find the average of a series of numbers")
    print()
    
    # Numbers to be averaged
    total_numbers = int(input("How many numbers are to be averaged: "))
    
    # Get numbers and the sum of the numbers
    average = 0
    for i in range(total_numbers):
        number = int(input(f"Enter number {i + 1}: "))
        average = (number + average) / (i + 1)
        print(f"The average numbers is {average:.2f}")
    
    # Average
    #average = total_sum / total_numbers
        
    #print(f"The average numbers is {average:.2f}")

main()
