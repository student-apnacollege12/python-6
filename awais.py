#import math

#def calcul_BMI():
   # height = float(input("enter height meters : "))
   # weight = float(input("Enter weight kg: "))
    #BMI Calculation

   # BMI = weight / (height ** 2)
    #print(BMI)
#calcul_BMI()



#def calcul_Volume():
   # radius = float(input("Enter radius cylinder: "))
   # height = float(input("Enter height cylinder: "))

    #volume calculation
   # Volume = math.pi * (radius ** 2) * height
   # return Volume
     
#output = calcul_Volume()   
#print(output) 





# Even or Odd
number = int(input("Enter a number"))
if number % 2 == 0:
    print("this is an even number ")
else:
    print("this is an odd number")    


# Positive,Negtive,Zero
    if number > 0:
        print(f"number is positive.")
    elif number < 0:
        print(f"number is negtive.") 
    else:
        print(f"number is zero.") 


#Divisibility by 2 and 3
    if number % 2 == 0 and number % 3 == 0:
        print(f"number is divisible by both 2 and 3.") 
    elif number % 2 == 0:
        print(f"number is divisible by 2.") 
    elif number % 3 == 0:
        print(f"number is divisible by 3.") 
    else:
        print(f"number is not divible by 2 or 3.") 


#Voting Eligibility
    age = int(input("Enter your age:"))   
    if age >= 18:
        nationality = input("Do you have Pakistani nationality? (yes/no):").lower() 
        if nationality == "yes":
            print("You are eligible to vote.")
        else:
            print("Please obtain a valid vote.")


# Age Category 
    age = int(input("Enter your age: "))
    if 0 <= age <= 12:
        print("Your are a Child.")  
    elif 13 <= age <= 19:
        print("Your are a teenager.")  
    elif 20 <= age <= 59:
        print("Your are an Adult.")  
    elif age >= 60:
        print("YOur are a senior citizen.") 
    else:
        print("Ivalid age entered.")


# Days in month
    month = int(input("Enter the month(1-12):")) 
    if month in[1,3,5,7,8,10,12]:
        print("This month has 31 days.") 
    elif month in [4,6,9,11]:
        print("This month has 30 days.")
    elif month == 2:
        print("This month has 28 days.")  
    else:
        print("Invalid month entered.") 


# checking for leap year
    year = int(input("Enter a year:"))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"year is a leap year.") 
    else:
        print(f"year is  not a leap year.")                                                      