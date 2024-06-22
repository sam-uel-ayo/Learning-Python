# A Fibonacci sequence is a sequence of numbers where each successive number is the sum of
# the previous two. The classic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13,. . .. Write a
# program that computes the nth Fibonacci number where n is a value input by the user. For
# example, if n = 6, then the result is 8.

def main():
    print("This program calculates the nth Fibonacci value.")
    print()


    n = int(input("Enter the value of n: "))
    curr, prev = 1, 1
    for i in range(n - 2):
        curr, prev = curr + prev, curr

    print(f"The {n}th Fibonacci number is: {curr}")

main()
