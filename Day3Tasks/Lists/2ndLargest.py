#8. Write a program to find the second largest number in a list.

num = [12,35,1,10,34,35]

distinct = sorted(set(num), reverse = True)

if len(distinct) >= 2:
    print("second largest:", distinct[1])
else:
    print("No second largest number")
