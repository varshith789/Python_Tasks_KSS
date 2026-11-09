#18. Write a function to find the sum of elements in a list using a user-defined function.

def list_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total


nums = list(map(int, input("Enter list elements separated by space:").split()))
print("sum of elements:", list_sum(nums))
