from datetime import datetime

# Function to calculate tire volume
def calculate_tire_volume(width, aspect_ratio, diameter):
    # Convert the tire dimensions from mm to meters and inches
    width_in_meters = width / 1000
    aspect_ratio_as_decimal = aspect_ratio / 100
    diameter_in_meters = diameter * 0.0254
    
    # Volume formula: V = (pi * (width^2) * aspect_ratio * (width + 2540 * diameter)) / 1000000000
    volume = (3.14159 * (width_in_meters ** 2) * aspect_ratio_as_decimal * (width_in_meters + 2540 * diameter_in_meters)) / 1000
    return round(volume, 2)

# Input values from the user
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume
volume = calculate_tire_volume(width, aspect_ratio, diameter)

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Append to volumes.txt file
with open("volumes.txt", "at") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

# Output the result to the user
print(f"The approximate volume is {volume} liters")