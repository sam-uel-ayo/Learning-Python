# The Gregorian epact is the number of days between January 1st and the previous new moon.
# This value is used to figure out the date of Easter. It is calculated by these formulas (using int #arithmetic):
#                             C = year//100
#             epact = (8 + (C//4) − C + ((8C + 13)//25) + 11(year%19))%30
#
# Write a program that prompts the user for a 4-digit year and then outputs the value of the epact.

def main():
    print("A program that gives the value of the epact from a 4-digit year")
    print()
    
    # Prompt user for a 4-digit year and convert it to an integer
    year = int(input("Enter a 4-digit year: "))

    # Calculate the century
    C = year // 100

    # Calculate the epact using the provided formula
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

    # Output the value of the epact
    print("The epact for the year", year, "is", epact)
    
main()
