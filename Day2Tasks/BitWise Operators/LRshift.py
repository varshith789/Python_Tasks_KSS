#4. Write a program to perform left shift (<<) and right shift (>>) operations on a number.
num =int(input("Enter a num:"))
n = int(input("Enter a shift positions:"))

left=num << n
right=num >> n

print("Left shift: ", left)
print("Right shift: ", right)
