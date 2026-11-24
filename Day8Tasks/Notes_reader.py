#Notes Reader Program

try:
    with open("notes.txt", "r") as f:
        content = f.read()
    print("Your Notes:\n")
    print(content)
except FileNotFoundError:
    print("notes.txt not found. Please create the file first.")
