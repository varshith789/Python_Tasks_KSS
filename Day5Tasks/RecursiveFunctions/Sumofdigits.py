#3. Write a recursive function to calculate the sum of digits of a number.
#Example: Input = 123 → Output = 6

def sum_of_digits(n):
    n =abs(n)
    if n== 0:
        return 0
    return (n%10) + sum_of_digits(n//10)

#function calling

num = int(input("Enter a number:"))

print(f"sum of digits of {num} = {sum_of_digits(num)}")
