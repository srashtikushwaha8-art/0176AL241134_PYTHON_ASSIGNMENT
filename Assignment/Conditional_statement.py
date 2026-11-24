# Question 1: Electricity Bill Calculator


units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

if bill > 2000:
    surcharge = bill * 5 / 100
    bill = bill + surcharge
    print("5% surcharge added:", surcharge)

print("Total electricity bill: Rs", bill)



# Question 2: Loan Approval System


salary = int(input("\nEnter salary: "))
credit_score = int(input("Enter credit score: "))
age = int(input("Enter age: "))

count = 0

if salary >= 30000:
    count = count + 1

if credit_score >= 700:
    count = count + 1

if age >= 21 and age <= 60:
    count = count + 1

if count == 3:
    print("Approved")
elif count == 2:
    print("Conditionally Approved")
else:
    print("Rejected")



# Question 3: Number Classification


number = int(input("\nEnter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# Question 4: Exam Result Analyzer


print()
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total marks:", total)
print("Percentage:", percentage)

if m1 < 33 or m2 < 33 or m3 < 33 or m4 < 33 or m5 < 33:
    print("Result: Fail")
else:
    print("Result: Pass")
    if percentage >= 60:
        print("Division: First")
    elif percentage >= 50:
        print("Division: Second")
    elif percentage >= 40:
        print("Division: Third")
    else:
        print("Passed, but no division (below 40%)")
