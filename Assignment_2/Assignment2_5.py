def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def main():
        n = int(input("Enter a number: "))
        if is_prime(n):
            print("It is Prime Number")
        else:
            print("It is not a Prime Number")
    
if __name__ == "__main__":
    main()