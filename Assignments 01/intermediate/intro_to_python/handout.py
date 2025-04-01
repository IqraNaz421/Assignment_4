
# Milestone #1: Mars Weight

# Prompt the user for their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Mars gravity constant (37.8% of Earth's gravity)
mars_gravity = 0.378

# Calculate weight on Mars
mars_weight = earth_weight * mars_gravity



# Print the result
print(f"The equivalent on Mars: {mars_weight}")



#part two


# Gravity constants for each planet (as percentages)
gravity_constants = {
    'Mercury': 0.376,
    'Venus': 0.889,
    'Mars': 0.378,
    'Jupiter': 2.360,
    'Saturn': 1.081,
    'Uranus': 0.815,
    'Neptune': 1.140
}

# Prompt the user for their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Prompt the user for a planet name
planet = input("Enter a planet: ")

# Check if the entered planet is valid and calculate weight on that planet
if planet in gravity_constants:
    # Get the gravity constant for the selected planet
    planet_gravity = gravity_constants[planet]
    
    # Calculate the weight on the selected planet
    planet_weight = earth_weight * planet_gravity
    
    # Round the result to two decimal places
    planet_weight_rounded = round(planet_weight, 2)
    
    # Print the result
    print(f"The equivalent weight on {planet}: {planet_weight_rounded}")
else:
    print("Invalid planet name. Please enter a valid planet.")

