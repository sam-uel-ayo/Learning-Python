# Write a program that determines the molecular weight of a hydrocarbon based on the number
# of hydrogen, carbon, and oxygen atoms. You should use the following weights:
#                 Atom  |  Weight(grams / mole)        
#                   H   |   1.0079
#                   C   |   12.011
#                   O   |   15.9994

def main():
    print("program that determines the molecular weight of a hydrocarbon")
    print("based on the number of hydrogen, carbon, and oxygen atoms")
    print()
    
    # Get the number of atoms
    carbon = float(input("What is number of Carbon atoms: "))
    hydrogen = float(input("What is number of Hydrogen atoms: "))
    oxygen = float(input("What is number of Oxygen atoms: "))
    
    # Calculate the molecular weight
    molecular_weight = (12.01 * carbon) + (1.01 * hydrogen) + (16.00 * oxygen)
    
    # Print the molecular weight
    print(f"The molecular weight of the hydrocarbon is: {molecular_weight:.2f} g/mol")
main()
