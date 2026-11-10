#String Reversal (without built-in reverse)

text = input("Enter a string:")

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)
             
