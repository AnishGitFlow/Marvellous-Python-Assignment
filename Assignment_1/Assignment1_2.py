# Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.

# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number

def ChkNum(number):
    if (number % 2 == 0):
        print("Even Number")
    else:
        print("Odd number")

ChkNum(11)
ChkNum(8)