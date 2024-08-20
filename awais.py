# inputs
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilogram: "))
# BMI Calculation
bmi =  weight/ (height  ** 2)
print(f"Your BMI is: {bmi:.2f}")
import math # math module
# inputs
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
# Volume Calculation
volume = math.pi * (radius ** 2) * height
print(f"The Volume of the cylinder is: {volume: .2f} cubic units")


