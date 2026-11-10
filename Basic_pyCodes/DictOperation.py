#Dictionary Operations

students = {"Rahul": 85, "Amit": 92, "Priya": 78}

# Add a new student
students["Sneha"] = 95

# Update existing student's marks
students["Priya"] = 82

# Print all student details
for name, marks in students.items():
    print(f"{name}: {marks}")
