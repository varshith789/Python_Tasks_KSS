#10. Write a program to remove duplicate characters from a string.


d = input("Enter a string")

result=""
for ch in  d:
    if ch not in result:
        result += ch
print("after removing duplicates:", result)
