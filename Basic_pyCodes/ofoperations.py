#5. List of Dictionaries

employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# 1. Employee with the highest salary
highest = max(employees, key=lambda e: e["salary"])
print("Highest salary:", highest)

# 2. Employees with salary greater than 35,000
high_earners = [e for e in employees if e["salary"] > 35000]
print("Salary > 35000:", high_earners)

# 3. Average salary
avg_salary = sum(e["salary"] for e in employees) / len(employees)
print("Average salary:", avg_salary)          # 45000.0

# 4. List of employee names
names = [e["name"] for e in employees]
print("Names:", names)                        # ['John', 'Alice', 'Bob', 'David']
