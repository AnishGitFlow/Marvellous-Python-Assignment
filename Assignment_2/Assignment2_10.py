def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10  
        n //= 10
    
    return total

def main():
        n = int(input("Enter a number: "))
        result = sum_of_digits(n)
        print(result)

if __name__ == "__main__":
    main()