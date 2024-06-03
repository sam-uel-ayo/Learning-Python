#Modify the Chaos program so that it prints out 20 values instead of 10



# A simple program illustrating chaotic behavior(modified to print out 20 values).
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20): # Changed the range of the loop from 10 to 20
        x = 3.9 * x * (1 - x)
        print(x)
main()
