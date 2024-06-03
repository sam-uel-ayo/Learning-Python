#  The calculation performed in the chaos program can be written in a number of ways that
#  are algebraically equivalent. Write a version of the chaos program for each of the following
#  ways of doing the computation. Have your modified programs print out 100 iterations of the
#  function and compare the results when run on the same input.
        #(a) 3.9 * x * (1 - x)
        #(b) 3.9 * (x - x * x)
        #(c) 3.9 * x - 3.9 * x * x
#  Explain the results of this experiment.



def a():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x * (1 - x)
        print(x)
a()

def b():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * (x - x * x)
        print(x)
b()

def c():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x - 3.9 * x * x
        print(x)
c()


#  The experiment demonstrates how even tiny variations in floating-point calculations can produce 
#  drastically different results in iterative procedures. Despite being algebraically similar, 
#  the order and structure of operations determine how accuracy errors develop. 
#  This is a typical problem in numerical computation and chaos theory, 
#  where minor differences can lead to dramatically divergent outcomes over time.
