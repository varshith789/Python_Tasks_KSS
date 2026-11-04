#8. Write a program to find the student with the highest marks from a dictionary.

std6 = {"Bunny": 94,"Ravi": 85,"Siddu": 90}

topper = max(std6, key=std6.get)
print("Highest marks:", topper, "-", std6[topper])
