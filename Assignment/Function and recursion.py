
# Question 1: Write a function to calculate factorial using a loop.


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


num = int(input("Enter a number for factorial: "))
print("Factorial of", num, "is", factorial(num))



# Question 2: Calculate the sum of first n natural numbers


def sum_of_n(n):
    if n == 0:                     
        return 0
    return n + sum_of_n(n - 1)      


n = int(input("\nEnter n: "))
print("Sum of first", n, "natural numbers is", sum_of_n(n))



# Question 3: Print a string in reverse using recursion.


def reverse_string(text):
    if text == "":                  
        return ""
    return reverse_string(text[1:]) + text[0]


word = input("\nEnter a string: ")
print("Reversed string:", reverse_string(word))


# Question 4: Find the power of a number (x ^ n) using recursion.


def power(x, n):
    if n == 0:                     
        return 1
    return x * power(x, n - 1)      


x = int(input("\nEnter base (x): "))
n = int(input("Enter power (n): "))
print(x, "to the power", n, "is", power(x, n))