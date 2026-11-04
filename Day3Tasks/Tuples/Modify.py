#7. Write a program to convert a tuple to a list and modify the element

t7 =(10,20,30,40)

temp = list(t7)

temp[1] = 98

t7 =tuple(temp)

print("modified tuple:",t7)
