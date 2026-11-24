
# Question 1: Palindrome String Check


text = input("Enter a string: ")


cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



# Question 2: Find the longest word in a sentence.


sentence = input("\nEnter a sentence: ")
words = sentence.split()

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)


# Question 3: Check whether two strings are anagrams.


first = input("\nEnter first string: ")
second = input("Enter second string: ")

first = first.replace(" ", "").lower()
second = second.replace(" ", "").lower()


if sorted(first) == sorted(second):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")



# Question 4: Remove duplicate characters from a string.


text = input("\nEnter a string: ")

result = ""
for ch in text:
    if ch not in result:
        result = result + ch

print("String without duplicates:", result)


# Question 5: Compress a string.


text = input("\nEnter a string to compress: ")

compressed = ""

if len(text) > 0:
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1
        else:
            compressed = compressed + text[i - 1] + str(count)
            count = 1

    
    compressed = compressed + text[-1] + str(count)

print("Compressed string:", compressed)