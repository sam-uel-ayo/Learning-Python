#Enter and run the Chaos program from Section 1.6(Chaos Program). Try it out with various values of input to
#see that it functions as described in the chapter.



# A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
main()
