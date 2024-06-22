#  Write a program to sum a series of numbers entered by the user. The program should first
#  prompt the user for how many numbers are to be summed. It should then input each of the
#  numbers and print a total sum.

def main():
    print("A program to sum a series of numbers")
    print()
    
    # Numbers are to be summed
    total_numbers = int(input("How many numbers are to be summed: "))
    
    # Get numbers are to be summed and sum
    total_sum = 0
    for i in range(total_numbers):
        number = int(input(f"Enter number {i + 1}: "))
        total_sum += number
        
    print(f"The total sum of numbers is {total_sum}")

main()