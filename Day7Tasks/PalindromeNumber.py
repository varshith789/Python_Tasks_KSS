#Palindrome number

num = int(input("Enter a number: "))

temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse =", reverse)
if reverse == num:
    print(f"{num} is a Palindrome number")
else:
    print(f"{num} is not a Palindrome number")
