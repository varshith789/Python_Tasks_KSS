#Stuents marks file analyser

total = 0
count = 0

try:
    with open("marks.txt", "r") as f:
        print("Student Records:")
        for line in f:
            line = line.strip()
            if line == "":
                continue                     # skip blank lines
            name, marks = line.split()
            print(f"{name} : {marks}")
            total += int(marks)
            count += 1

    if count > 0:
        print(f"\nAverage Marks of the Class: {total / count:.2f}")
    else:
        print("No records found in the file.")
except FileNotFoundError:
    print("marks.txt not found.")
