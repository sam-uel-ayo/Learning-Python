#Modify the Chaos program using 2.0 in place of 3.9 as the multiplier in the logistic function.
#Your modified line of code should look like this:
            #x = 2.0 * x * (1 - x)
#Run the program for various input values and compare the results to those obtained from the
#original program. Write a short paragraph describing any differences that you notice in the
#behavior of the two versions.



def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x) #Modified 3.9 to 2.0
        print(x)
main()

# The original program was truly chaotic and the results had to no visible pattern but in contrast
# to the modified program with the change of the multiplier value from 3.9 to 2.0 the result of the 
# program became predict - that repeated values would occur, and a pattern became visible.