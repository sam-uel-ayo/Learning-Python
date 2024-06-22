# Write a program to determine the length of a ladder required to reach a given height when
# leaned against a house. The height and angle of the ladder are given as inputs. To compute
# length use
#                 length = height / sin angle
#

import math
def angle_sin(angle):
    # Convert angle to radian
    angle_rad = angle * (math.pi / 180)

    # Get the Sine of the angle
    angle_sin = math.sin(angle_rad)
    return angle_sin

def main():
    print("A a program to determine the length of a ladder required to reach a given height")
    print("when leaned against a house")
    print()
    
    # Get the height and angle 
    height = float(input("What is the height of the ladder (In meters): "))
    angle = float(input("What is the angle (In degrees): "))
    
    # Calculate the length
    length = height / angle_sin(angle)
    
    print(f"The length of the ladder is {length:.2f} meters")
main()

