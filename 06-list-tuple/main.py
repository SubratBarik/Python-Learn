""" List & Tuple """

MARKS = [25, 63.5, 90, 87, 75, 55, 67]

print("Marks: ", MARKS)
print("Value of marks at index 5:",MARKS[5])
print("Length of Marks: ", len(MARKS))
print("Type of the Mark: ", type(MARKS))
MARKS[6] = 49 #adding a new item at the end
MARKS[4] = 30 #replacing a item with new one
print("Marks: ", MARKS)
print("Sliced List: ", MARKS[1:5]) #slicing from index 1 to 5
MARKS.append(11)
print("Appened 11 in Marks list: ", MARKS) #Append 11
print(MARKS.sort())
print("ASC order using Sort: ", MARKS)
#print("ASC Sort: ", MARKS)
