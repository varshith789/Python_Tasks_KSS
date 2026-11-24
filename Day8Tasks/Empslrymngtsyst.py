#Employee salary management system

employees = []

try:
    # Read and display all employees
    with open("employees.txt", "r") as f:
        print("Employee Details:")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            name, salary = line.split()
            employees.append((name, int(salary)))
            print(f"{name} : {salary}")

    # Find highest salary
    if employees:
        top = max(employees, key=lambda e: e[1])
        print(f"\nHighest Salary: {top[0]} - {top[1]}")

    # Append a new employee
    new_name = input("\nEnter new employee name: ")
    new_salary = int(input("Enter salary: "))

    with open("employees.txt", "r") as f:
        content = f.read()
    with open("employees.txt", "a") as f:
        if content and not content.endswith("\n"):
            f.write("\n")                    # make sure new record starts on a new line
        f.write(f"{new_name} {new_salary}\n")

    print("Employee record added successfully.")

except FileNotFoundError:
    print("employees.txt not found.")
except ValueError:
    print("Invalid input! Salary must be a number.")
