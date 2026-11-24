#Grocery list manager

n = int(input("How many items do you want to add? "))

with open("grocery.txt", "w") as f:         # "w" = write (overwrites old list)
    for i in range(n):
        item = input(f"Enter item {i + 1}: ")
        f.write(item + "\n")                # each item on a new line

print("\nGrocery list saved. File contents:")
with open("grocery.txt", "r") as f:
    print(f.read())
