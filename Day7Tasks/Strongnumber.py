#Strong number

num = int(input("Enter a number: "))

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += factorial(digit)    # factorial of each digit
    temp //= 10

if total == num:
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a Strong number")
