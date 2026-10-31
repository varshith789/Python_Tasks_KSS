#3. Write a program to find the sum of numbers from 1 to N using a loop.

n = int(input("Enter a number:"))
Sum = 0

for i in range(1,n+1):
    Sum = Sum + i

print("sum:",Sum)
