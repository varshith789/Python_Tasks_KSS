#1. Write a recursive function to calculate the factorial of a number.

def factorial(n):
    if n<0:
        return "Not defined"
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1) #recursive fun

num = int(input("Enter a number:"))

print(f"Factorial of {num} = {factorial(num)}")
