# Question 1: Age Validation System


class AgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("Age is valid")

except AgeError as error:
    print("Error:", error)
except ValueError:
    print("Error: Please enter a number")



# Question 2: Bank Withdrawal System


class InsufficientBalanceError(Exception):
    pass


balance = 5000
print("\nCurrent balance:", balance)

try:
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        raise InsufficientBalanceError("Withdrawal amount is more than the balance")

    balance = balance - amount
    print("Withdrawal successful. New balance:", balance)

except InsufficientBalanceError as error:
    print("Error:", error)
except ValueError:
    print("Error: Please enter a valid amount")



# Question 3: Password Validator


class PasswordTooShortError(Exception):
    pass


class NoUppercaseError(Exception):
    pass


class NoNumberError(Exception):
    pass


password = input("\nEnter a password: ")

try:
    
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters long")

   
    has_uppercase = False
    for ch in password:
        if ch.isupper():
            has_uppercase = True

    if not has_uppercase:
        raise NoUppercaseError("Password must have at least one uppercase letter")

   
    has_number = False
    for ch in password:
        if ch.isdigit():
            has_number = True

    if not has_number:
        raise NoNumberError("Password must have at least one number")

    print("Strong password")

except PasswordTooShortError as error:
    print("Error:", error)
except NoUppercaseError as error:
    print("Error:", error)
except NoNumberError as error:
    print("Error:", error)
