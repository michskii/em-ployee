import math

# Function to calculate sin, cos, and tan of an angle in degrees
def calculate_trigonometric_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    return sin_value, cos_value, tan_value

# Input: Angle in degrees
angle = float(input("Enter the angle in degrees: "))

# Calculate and display the results
sin_val, cos_val, tan_val = calculate_trigonometric_values(angle)
print(f"sin({angle}) = {sin_val}")
print(f"cos({angle}) = {cos_val}")
print(f"tan({angle}) = {tan_val}")