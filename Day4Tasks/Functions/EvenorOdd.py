#15. Write a function to check whether a number is even or odd.

def isevenorodd(n):
    return "Even" if n%2 == 0 else "odd"

#even or odd

n = int(input("Enter a number:"))
print(f"{n} is {isevenorodd(n)}")
