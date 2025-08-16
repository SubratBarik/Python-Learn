""" List & Tuple """

# Lists : usess square brackets
MARKS = [25, 63.5, 90, 87, 75, 55, 67]
FRUITS = ["Banana", "Mango", "Litchi", "Watermelon", "Grapes"]

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
print(MARKS.sort()) #ASC Sort
print("ASC order using Sort: ", MARKS)
print(MARKS.sort(reverse=True)) #DESC Sort
print("DESC order using Sort: ", MARKS)
print(FRUITS.sort()) #ASC Sort
print("ASC order using Sort: ", FRUITS)
FRUITS.sort(reverse=True) #Sorting in DESC
print("DESC order using Sort: ", FRUITS) #DESC Sort
FRUITS.reverse() # reverse the list
print("Reverse of list items: ", FRUITS)
print(FRUITS.remove("Litchi")) #remove an item
print("Remove an item from list items by item itself: ", FRUITS)
print("Remove an item from list items by Index: ", FRUITS.pop(3))
print("================================")
# Tuples : uses paranthesis
BOOKS = ("A", "B", "C", "D", "E")
print(BOOKS)
