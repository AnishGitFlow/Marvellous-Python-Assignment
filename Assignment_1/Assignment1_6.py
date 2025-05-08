# Includes a function to check if a number is positive, negative, or zero

def CheckNumber(number):
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

def main():
    CheckNumber(11)
    CheckNumber(-8)
    CheckNumber(0)

if __name__ == "__main__":
    main()