# Has ChkNum() function that checks if a number is even or odd

def ChkNum(number):
    if (number % 2 == 0):
        print("Even Number")
    else:
        print("Odd number")

def main():
    ChkNum(11)
    ChkNum(8)

if __name__ == "__main__":
    main()