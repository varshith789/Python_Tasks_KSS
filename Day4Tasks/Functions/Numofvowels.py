#19. Write a function that takes a string as input and returns the number of vowels.


def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

s = input("Enter a string:")
print("Number of vowels:", count_vowels(s))
