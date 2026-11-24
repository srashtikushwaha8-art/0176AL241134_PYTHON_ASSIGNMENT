
# Question 1: Use the math module.


import math 

number = int(input("Enter a number: "))

print("Square root:", math.sqrt(number))
print("Power (number ^ 2):", math.pow(number, 2))
print("Factorial:", math.factorial(number))

angle = 30
radians = math.radians(angle)        # sin, cos, tan need radians
print("sin(30):", round(math.sin(radians), 2))
print("cos(30):", round(math.cos(radians), 2))
print("tan(30):", round(math.tan(radians), 2))



# Question 2: Use the random module.

import random
import string

# 6 digit OTP
otp = ""
for i in range(6):
    otp = otp + str(random.randint(0, 9))
print("\nOTP:", otp)

# Random password of 8 characters (letters, digits and symbols)
characters = string.ascii_letters + string.digits + "@#$%&"
password = ""
for i in range(8):
    password = password + random.choice(characters)
print("Random password:", password)

# List of 5 random numbers between 1 and 100
random_list = []
for i in range(5):
    random_list.append(random.randint(1, 100))
print("Random list:", random_list)


# Question 3: Use the datetime module.


import datetime

now = datetime.datetime.now()
print("\nCurrent date and time:", now.strftime("%d-%m-%Y %H:%M:%S"))

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day: "))

today = datetime.date.today()
age = today.year - birth_year


if (today.month, today.day) < (birth_month, birth_day):
    age = age - 1

print("Your age is:", age, "years")


# Question 4: Create a package "geometry" with modules


from geometry import circle, rectangle

radius = float(input("\nEnter radius of circle: "))
print("Circle area:", round(circle.area(radius), 2))
print("Circle circumference:", round(circle.circumference(radius), 2))

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print("Rectangle area:", rectangle.area(length, width))
print("Rectangle perimeter:", rectangle.perimeter(length, width))