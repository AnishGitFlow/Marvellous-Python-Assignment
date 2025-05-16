# Has a function that returns True if a number is divisible by 5

def CheckDivisible(number):
    return number % 5 == 0

def main():
    result1 = CheckDivisible(8)
    result2 = CheckDivisible(25)

    print(f"Input: 8")
    print(f"Output: {result1}")

    print(f"Input: 25")
    print(f"Output: {result2}")

if __name__ == "__main__":
    main()