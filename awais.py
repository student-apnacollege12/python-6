#import math
#radius = float(input("Enter a radius of the circle"))
#area = math.pi * radius * radius

#print("the area of a circle", area)




#count : int = 1
#while count <=100:
   # print("hello world",count)
   # count = count + 10




#Function to insert a value at a specific indexin an array.
def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr
my_array = [1,2,3,4]
updated_array = insert_value(my_array, 2, 10)
print(updated_array)


#Simple shopping cart program
cart = []

def add_item(item):
    cart.append(item)
    print(f"item '{item}' added to the cart.")

    def remove_item(item):
        if item in cart:
            cart.remove(item)
            print(f"item '{item}' removed from the cart.")
        else:
            print(f"item '{item}' not found in the cart.")

    def updated_quantity(item, quantity):
        if item in cart:
            index = cart.index(item)
            cart[index] = (item, quantity)
            print(f"item '{item}' quantity updated to {quantity}.") 
        else:
            print(f"item '{item}' not found in the cart.")
    def view_cart():
        print("cart contents:")
        for item in cart:
            print(item)

    add_item('apple') 
    add_item('banana')
    view_cart() 
    updated_quantity('banan', 5) 
    view_cart()
    remove_item('apple')
    view_cart()     


    #program to print the first 25 integers using a while loop.
    i = 1
    while i <= 25:
        print(i)  
        i += 1


    #program to print the first 10 even numbers using a while loop.
    i = 2
    count = 0
    while count < 10:
        print(i) 
        i += 2
        count += 1


    #function to calculate the factorial of a number using a while loop.
    def factorial(n):
        result = 1
        while n > 0:
            result *= n
            n -= 1
        return result
    print(factorial(5))


    #program to remove negative numbers from an array.
    numbers = [1,-2,3,-4,5,-6] 
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            numbers.pop(i)  
        else:
            i += 1
    print(numbers)  


    #function to calculate the sum of numbers in an aray using a while loop.
    def sum_of_array(arr):
        total = 0
        i = 0
        while i < len(arr):
            total += arr[i] 
            i += 1
        return total
    print(sum_of_array([1,2,3,4,5])) 


    #programto convert celsius temperatures to fahrenheit
    def celsius_to_fahrenheit(temperatures):
        fahrenheit = []
        i = 0
        while i < len(temperatures):
            f = (temperatures[i] *9/5 + 32)
            fahrenheit.append(f)
            i += 1
        return fahrenheit

    celsius_temperatures = [0,20,37,100]  
    converted_temps = celsius_to_fahrenheit(celsius_temperatures)
    print(converted_temps)


    #program to remove all odd numbers from an array.
    numbers = [1,2,3,4,5,6,7,8,9]
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 != 0:
            numbers.pop(i)
        else:
            i += 1
    print(numbers)        
