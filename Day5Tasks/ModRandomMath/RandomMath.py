#4. Write a Python program that generates 20 random numbers between 1 and 200 using
#the random module and store them in a list.
#● Maximum value● Minimum value● Square root of the maximum number● Logarithm of the minimum number

import math
import random

numbers = [random.randint(1,200) for i in range(20)]

print("Numbers:",numbers)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("sqaure root of max:",math.sqrt(maximum))
print("Logarithm of min:",math.log(minimum))
