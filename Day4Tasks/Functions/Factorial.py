#16. Write a function that returns the factorial of a number.

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n+1):
        result*= i
    return result

#factorial of number

n = int(input("enter a number:"))
res = factorial(n)
if res is None:
    print("Factorial is not defined for negative numbers:")
else:
    print(f"Factorial of {n} is {res}")
