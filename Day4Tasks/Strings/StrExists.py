#5. Write a program to check whether a substring exists in a string.

s = input("Enter a string:")

sub = input("Enter a sub string to search:")

if sub in s:
    print(f"'{sub}' exists in the string.")

else:
    print(f"'{sub}' doesnot exists in the string.")
    
