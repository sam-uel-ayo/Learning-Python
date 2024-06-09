# Modify the futval.py program (Section 2.7) so that the number of years for the investment
# is also a user input. Make sure to change the final message to reflect the correct number of
# years.
#        # futval.py
#        # A program to compute the value of an investment
#        # carried 10 years into the future
#        def main():
#            print("This program calculates the future value")
#            print("of a 10-year investment.")
#
#            principal = eval(input("Enter the initial principal: "))
#            apr = eval(input("Enter the annual interest rate: "))
#
#            for i in range(10):
#                principal = principal * (1 + apr)
#
#            print("The value in 10 years is:", principal)
#        main()
#


def main():
    print("This program calculates the future value")
    print("of a n-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter duration of investment(Years): "))

    for i in range(year):
        principal = principal * (1 + apr)

    print("The value in", year, "years is:", principal)
main()

