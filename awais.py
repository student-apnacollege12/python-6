
def calcul_bmi():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))

   # BMI calculation
    bmi  = weight / (height ** 2)
    print(bmi)
    
calcul_bmi()


import math
def calcul_volume():
    radius = float(input("Enter  radius cylinder: "))
    height = float(input("Enter height cylinder: "))

    #valume calculation
    Volume = math.pi * (radius ** 2) * height
    print(Volume)

calcul_volume()    

