#Armstrong number

num = int(input("Enter a number: "))

temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** 3      # cube of each digit
    temp //= 10

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
