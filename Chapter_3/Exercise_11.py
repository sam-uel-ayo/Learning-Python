# Write a program to find the sum of the first n natural numbers, where the value of n is
# provided by the user.

def main():
    print("A program to find the sum of the first n natural numbers")
    print()
    
    # Get natural numbers
    number = int(input("Enter the number: "))
    
    # Calulate the sum of natural numbers
    total_sum = 0
    for i in range(1, number + 1):
        total_sum += i
        
    print(f"The sum of the first {number} natural numbers is {total_sum}")
    
main()
