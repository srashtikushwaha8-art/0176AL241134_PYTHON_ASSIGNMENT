
# Question 1: Automorphic Number


number = int(input("Enter a number: "))
square = number * number

digits = 0
temp = number
while temp > 0:
    digits = digits + 1
    temp = temp // 10

last_digits = square % (10 ** digits)

if last_digits == number:
    print(number, "is an Automorphic number (square =", square, ")")
else:
    print(number, "is not an Automorphic number (square =", square, ")")



# Question 2: Palindrome Number Series


start = int(input("\nEnter start of range: "))
end = int(input("Enter end of range: "))

print("Palindrome numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    original = num
    reverse = 0

    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10

    if original == reverse:
        print(original, end=" ")

print()



# Question 3: LCM and HCF using loops (without built-in functions)


a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))


if a < b:
    smaller = a
else:
    smaller = b

hcf = 1
for i in range(1, smaller + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

if a > b:
    lcm = a
else:
    lcm = b

while lcm % a != 0 or lcm % b != 0:
    lcm = lcm + 1

print("HCF of", a, "and", b, "is", hcf)
print("LCM of", a, "and", b, "is", lcm)



# Question 4: Password Retry System


correct_password = "python123"
attempts = 0
login_success = False

while attempts < 3:
    password = input("\nEnter password: ")

    if password == correct_password:
        login_success = True
        break
    else:
        attempts = attempts + 1
        print("Wrong password. Attempts left:", 3 - attempts)

if login_success:
    print("Login successful")
else:
    print("Account blocked after 3 failed attempts")



# Question 5: Print different star patterns


rows = int(input("\nEnter number of rows for patterns: "))

print("\nTriangle:")
for i in range(1, rows + 1):
    print("*" * i)


print("\nPyramid:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


print("\nDiamond:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))