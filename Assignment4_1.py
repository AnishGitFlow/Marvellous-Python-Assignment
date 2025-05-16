def main():
    power_of_two = lambda x: x ** 2
    
    num = int(input("Enter a number to get its power of two: "))
    result = power_of_two(num)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()