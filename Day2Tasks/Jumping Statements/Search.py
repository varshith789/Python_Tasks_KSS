#4. Write a program that searches for a number in a list and breaks the loop when found.
num = [10,20,30,40,50]

search = int(input("enter number to search:"))

for i in num:
    if i == search:
        print("Number found:")
        break
else:
    print("Number not found:")
