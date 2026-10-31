#5. Write a program to calculate the factorial of a number using a loop.

num = int(input("Enter number:"))
fact = 1

for i in range(1,num+1):
    fact = fact*i
print("Factorial=",fact)
