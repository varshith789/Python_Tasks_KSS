#2. Write a recursive function to find the nth Fibonacci number.


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0: # base case 1
        return 0
    if n == 1: # base case 2
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) # recursive case


n = int(input("Enter n: "))
print(f"The {n}th Fibonacci number = {fibonacci(n)}")
