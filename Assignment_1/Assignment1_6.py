# Write a python program which accept number from user and check whether that number is positive or negative or zero.

# Input : 11    Output : Positive Number
# Input : -8    Output : Negative Number
# Input : 0    Output : Zero

print("Enter your number : ")
number = int(input())

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")