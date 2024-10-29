# if statement
# store data list, tuple , dictionary and set
#loop


entered_value = input("enter a number: ")
print(type(entered_value))

if not entered_value.isnumeric():
    print("enter a valid number")
    exit(0)

score = int(entered_value)
if score >= 78:
    print("A")

elif 71 <= score < 78:
    print("A-")
elif 64 <= score < 70:
    print("B+")
elif 57 <= score <= 63:
    print("B")
elif 50 <= score <= 56:
    print("B-")
elif 45 <= score <= 49:
    print("C+")
elif 40 <= score <= 44:
    print("C")
else:
    print("C-")