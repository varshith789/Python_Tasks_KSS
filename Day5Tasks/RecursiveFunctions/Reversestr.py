#4. Write a recursive function to reverse a string.


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0] # reverse the rest, then add first char


text = input("Enter a string: ")
print("Reversed string:", reverse_string(text)) 
