#20. Write a Python program with a function that returns the largest of three numbers.

def largest_of_three(a, b, c):
    if a>= b and a>=c:
        return a
    elif b >= a and b >= c:
        return b
    return c

a = float(input("Enter first number:"))

b = float(input("Enter second number:"))

c = float(input("Enter third number:"))

print("Largest :", largest_of_three(a, b, c))
