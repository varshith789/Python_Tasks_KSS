#3. Common Elements Using Sets

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

print("Common elements:", set1 & set2)          # {3, 4, 5}
print("Only in first list:", set1 - set2)        # {1, 2}
print("All unique elements:", set1 | set2)       # {1, 2, 3, 4, 5, 6, 7}
