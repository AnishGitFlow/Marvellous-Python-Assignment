def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    numbers = list(map(int, input("Enter list: ").split()))
    primes = list(filter(is_prime, numbers))
    print(f"Prime numbers: {primes}")

if __name__ == "__main__":
    main()