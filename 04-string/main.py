"""This module demonstrates string assignment and printing."""

STR_1 = "This is a string"
STR_2 = "Subrat's daughter's name is \nShreya or Chiku sona"
STR_3 = "and has been concatenated with other string"

print(STR_1) #printing string
print(STR_2) #printing string

RESULT = STR_1 +" "+ STR_3  #concatenation

print(RESULT, "\nTotal characters:",len(RESULT)) # concatenation & finding length

print(STR_1[5]) #indexing

print(STR_1[0:9]) #slicing
print(STR_1[5:]) #another way of slicing
print(STR_1[-3:-1]) #another way of slicing

print(STR_1.endswith("ing")) #finds in the string

STR_4 = "herosima"
STR_5 = STR_4.capitalize() #capitalize
print(STR_5)

print(STR_1.replace("string", "kelma")) #replaces a word or character in a string

print(STR_1.find("string")) #finding the first index of the string

print(STR_1.count("i"))

VAR_1 = input("Write a sentence")

print("Sentense entered is of length: ", len(VAR_1))
