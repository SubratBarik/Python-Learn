"""conditional statement"""

TOTAL_MARKS = input("Enter your total marks out of 100: ")
TOTAL_MARKS = int(TOTAL_MARKS)
if TOTAL_MARKS >= 90:
    print("You have secured Grade A")
elif TOTAL_MARKS < 90 and TOTAL_MARKS >= 80:
    print("You have secured Grade B")
elif TOTAL_MARKS < 80 and TOTAL_MARKS >= 70:
    print("You have secured Grade C")
elif TOTAL_MARKS < 70 and TOTAL_MARKS >= 60:
    print("You have secured Grade D")
elif TOTAL_MARKS < 60 and TOTAL_MARKS >= 35:
    print("You have secured Grade E")
else:
    print("You have Failed")
