#2. Write a recursive function to find the nth Fibonacci number

def fibonacci(n):

    if n<0:
        raise ValueError("n must be Non Negative")
    if n==0:
        return 0
    if n ==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#calling function

n = int(input("Enter n:"))

print(f"The{n}th Fibonacci number = {fibonacci(n)}")
