#10. Print a table row using formatted strings
item , qty , cost = "pen", 10, 5.5
print(f"{'item':<10}{'qty':>5}{'cost':>8}")
print(f"{item:<10}{qty:>5}{cost:>8.2f}")
