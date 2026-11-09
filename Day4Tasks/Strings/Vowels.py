#6. Write a program to count the number of vowels in a string.


s = input("Enter a string")

count = sum(1 for ch in s.lower() if ch in "aeiou")
print("Numer of vowels is :", count)
