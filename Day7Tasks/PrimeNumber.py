#Prime number

num = int(input("Enter a number: "))

factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print("Factors =", ", ".join(map(str, factors)))

if len(factors) == 2:        # only 1 and itself
    print(f"{num} is a Prime number")
else:
    print(f"{num} is not a Prime number")
