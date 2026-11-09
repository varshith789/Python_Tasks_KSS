#8. Write a program to check whether a string is a palindrome.

p = input("Enter a string to check whether it is palindrome:")

cleaned = p.replace(" ","").lower()
if cleaned == cleaned[::-1]:
    print("It is a palindrome")
else:
    print("It is not palindrome")
