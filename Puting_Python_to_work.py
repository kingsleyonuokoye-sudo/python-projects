# Ask the user to enter the radius of the circle
radius = float(input("What is the radius of the circle? "))

# Store the value of Pi
pi = 3.14

# Calculate the diameter
diameter = 2 * radius

# Calculate the circumference
circumference = 2 * pi * radius

# Calculate the area
area = pi * (radius ** 2)

# Display the results to the user
print(
    f"\nA circle with a radius of {radius:g} units will have a diameter of "
    f"{diameter:g} units, a circumference of {circumference:.2f} units, "
    f"and an area of {area:.2f} square units."
)
