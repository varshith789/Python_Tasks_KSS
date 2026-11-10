# MEDIUM LEVEL
#Q1. Remove Duplicates (preserving order, no set)

lst = [1, 2, 3, 2, 4, 1, 5, 3]

result = []
for item in lst:
    if item not in result:
        result.append(item)

print(result)   # [1, 2, 3, 4, 5]

