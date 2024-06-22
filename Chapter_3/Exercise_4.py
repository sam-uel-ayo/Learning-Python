# Write a program that determines the distance to a lightning strike based on the time elapsed
# between the flash and the sound of thunder. The speed of sound is approximately 1100 ft/sec
# and 1 mile is 5280 ft.

def calculate_lightning_distance(time_elapsed):
    # Speed of sound in feet per second
    speed_of_sound = 1100
    # Number of feet in a mile
    feet_per_mile = 5280
    
    # Calculate the distance in feet
    distance_in_feet = time_elapsed * speed_of_sound
    
    # Convert the distance to miles
    distance_in_miles = distance_in_feet / feet_per_mile
    
    return distance_in_miles

def main():
    print("A program that determines the distance to a lightning strike")
    print("based on the time elapsed between the flash and the sound of thunder.")
    
    # Input: Time elapsed between flash and thunder
    time_elapsed = float(input("Enter the time elapsed between the lightning flash and the thunder (in seconds): "))

    # Calculate and print the distance
    distance = calculate_lightning_distance(time_elapsed)
    print(f"The lightning strike is approximately {distance:.2f} miles away.")

main()
