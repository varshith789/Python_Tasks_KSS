
from utilities import MathOperations

from utilities import StringOperations

print("sum:", MathOperations.add(10,20))

print("Product:", MathOperations.multiply(10,20))

word = input("Enter a string:")

print("Uppercase:",StringOperations.to_uppercase(word))

print("Number of characters:",StringOperations.count_char(word))
