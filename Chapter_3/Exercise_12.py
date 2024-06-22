#  Write a program to find the sum of the cubes of the first n natural numbers where the value
#  of n is provided by the user.

def main():
    print("A program to find the sum of the cube of the first n natural numbers")
    print()
    
    # Get natural number
    number = int(input("Enter the number: "))
    
    # Calulate the sum of the cubes of natural numbers
    total_sum = 0
    for i in range(1, number + 1):
        total_sum += i ** 3
        
    print(f"The sum of the cube of the first {number} natural numbers is {total_sum}")
    
main()