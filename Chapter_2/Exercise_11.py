# Write an interactive Python calculator program. The program should allow the user to type a
# mathematical expression, and then print the value of the expression. Include a loop so that
# the user can perform many calculations (say, up to 100). Note: to quit early, the user can
# make the program crash by typing a bad expression or simply closing the window that the
# calculator program is running in.

def main():
    print("An interactive Python calculator program")
    print("Type a bad expression to close!")
    
    for i in range(101):
        ans = eval(input("Enter an expression: "))
        print(ans)

main()