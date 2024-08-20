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
current_year = 2024
birth_year = 2004
age = current_year - birth_year
print("This is my age",age)
lenght = 10
width = 5
print("The area of the rectangle is:", lenght * width)
print(3.14 * 7 ** 2)
print((98 - 32) * 5 / 9)
print((37 * 9 / 5) + 32)
print(divmod(125, 60))
print((400 / 500) * 100)
