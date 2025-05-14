def sum_of_factors(n):
    if n <= 0:
        return "Enter a positive number"
    
    factor_sum = 0
    for i in range(1, n): 
        if n % i == 0:
            factor_sum += i
    
    return factor_sum

def main():
        n = int(input("Enter a number: "))
        result = sum_of_factors(n)
        print(result)
    
if __name__ == "__main__":
    main()