def calculate_factorial(n):
    if n < 0:
        return "Negative numbers not allowed"
    
    if n == 0 or n == 1:
        return 1
    
    factorial = 1
    for i in range(2, n + 1):
        factorial = factorial * i
    
    return factorial

def main():
        n = int(input("Enter a number: "))
        result = calculate_factorial(n)
        print(result)
    
if __name__ == "__main__":
    main()