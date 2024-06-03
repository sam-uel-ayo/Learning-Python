#  (Advanced) Modify the Chaos program so that it accepts two inputs and then prints a table
#  with two columns similar to the one shown in Section 1.8. (Note: You will probably not be
#  able to get the columns to line up as nicely as those in the example. Chapter 5 discusses how
#  to print numbers with a fixed number of decimal places.)
#            input     0.25    0.26
#            --------------------------
#                   0.731250 0.750360
#                   0.766441 0.730547
#                   0.698135 0.767707
#                   0.821896 0.695499
#                   0.570894 0.825942
#                   0.955399 0.560671
#                   0.166187 0.960644
#                   0.540418 0.147447
#                   0.968629 0.490255
#                   0.118509 0.974630


def main():
    print("This program illustrates a chaotic function between two values")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    
    print("input     " + str(x) + "    " + str(y))
    print("--------------------------")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("        "f"{x:.6f}  {y:.6f}")
main()
