#Perfect Number

num = int(input("Enter a number: "))

divisors = []
for i in range(1, num):      # proper divisors exclude the number itself
    if num % i == 0:
        divisors.append(i)

total = sum(divisors)
print("Divisors:", ", ".join(map(str, divisors)))
print("Sum =", " + ".join(map(str, divisors)), "=", total)

if total == num:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")
