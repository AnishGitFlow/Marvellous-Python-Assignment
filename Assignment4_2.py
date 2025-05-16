def main():
    multiply = lambda x, y: x * y
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = multiply(num1, num2)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()