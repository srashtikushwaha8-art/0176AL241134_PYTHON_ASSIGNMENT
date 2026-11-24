
# Question 1: List Rotation


numbers = [1, 2, 3, 4, 5, 6]
k = int(input("Enter k (number of positions): "))
direction = input("Rotate left or right? ").lower()


k = k % len(numbers)

if direction == "left":
    rotated = numbers[k:] + numbers[:k]
else:
    rotated = numbers[len(numbers) - k:] + numbers[:len(numbers) - k]

print("Original list:", numbers)
print("Rotated list :", rotated)



# Question 2: Remove Duplicates without Set


items = [4, 2, 4, 7, 2, 9, 7, 1]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("\nOriginal list      :", items)
print("List without duplicates:", unique_items)



# Question 3: Find Missing Number


given_list = [1, 2, 3, 5, 6, 7, 8]

n = len(given_list) + 1                
expected_sum = n * (n + 1) // 2         
actual_sum = sum(given_list)

missing_number = expected_sum - actual_sum
print("\nList:", given_list)
print("Missing number:", missing_number)



# Question 4: Create a tuple of 5 subjects and:


subjects = ("Maths", "Physics", "Chemistry", "English", "Computer")

print("\nSubjects:", subjects)
print("Third subject:", subjects[2])
print("Total subjects:", len(subjects))
print("Index of English:", subjects.index("English"))



# Question 5: Convert Tuple to Dictionary


pairs = ((1, "A"), (2, "B"), (3, "C"))
result_dict = {}

for key, value in pairs:
    result_dict[key] = value

print("\nTuple     :", pairs)
print("Dictionary:", result_dict)



# Question 6: Tuple Unpacking Logic


data = (10, 20, 30, 40, 50)

first, *middle, last = data
swapped = (last, *middle, first)

print("\nOriginal tuple:", data)
print("Swapped tuple :", swapped)



# Question 7: Subset Checker


set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print("\nSet A:", set_a)
print("Set B:", set_b)

if set_a.issubset(set_b):
    print("Set A is a subset of Set B")
else:
    print("Set A is not a subset of Set B")


# Question 8: Student Marks Analyzer


students = {
    "Amit": 78,
    "Riya": 92,
    "Karan": 30,
    "Neha": 65,
    "Rohan": 28
}

topper_name = ""
topper_marks = 0
total_marks = 0
failed_students = []

for name in students:
    marks = students[name]
    total_marks = total_marks + marks

    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

    if marks < 33:
        failed_students.append(name)

average = total_marks / len(students)

print("\nTopper  :", topper_name, "with", topper_marks, "marks")
print("Average :", average)
print("Failures:", failed_students)



# Question 9: Library Management using Dictionary


library = {
    "Python Basics": 5,
    "Data Structures": 3,
    "Web Development": 2
}

print("\nBooks in library:", library)


new_book = input("Enter a new book name to add: ")
new_quantity = int(input("Enter its quantity: "))

if new_book in library:
    library[new_book] = library[new_book] + new_quantity
else:
    library[new_book] = new_quantity


issue_book = input("Enter the book name to issue: ")

if issue_book in library and library[issue_book] > 0:
    library[issue_book] = library[issue_book] - 1
    print("Book issued:", issue_book)
else:
    print("Sorry, this book is not available")

return_book = input("Enter the book name to return: ")

if return_book in library:
    library[return_book] = library[return_book] + 1
    print("Book returned:", return_book)
else:
    print("This book does not belong to our library")

print("Final library stock:", library)