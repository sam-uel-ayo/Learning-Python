# Suppose you have an investment plan where you invest a certain fixed amount every year.
# Modify futval.py to compute the total accumulation of your investment. The inputs to the
# program will be the amount to invest each year, the interest rate, and the number of years for
# the investment.
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
            print("This program calculates the future value of an")
            print("n-year investment.")

            annual_investment = eval(input("Enter your annual investment amount: "))
            apr = eval(input("Enter the annual interest rate: "))
            years = eval(input("Enter duration of investment(Years): "))

            total_amount = 0
            for i in range(years):
                total_amount = total_amount + annual_investment   # Add annual investment first
                total_amount = total_amount * (1 + apr)           # Then apply interest

            print("The value in", years, "years is:", total_amount)
            
main()