import MarvellousNum

def ListPrime(elements):
    return [num for num in elements if MarvellousNum.ChkPrime(num)]

def sum_of_prime_elements():
    n = int(input("Input: Number of elements: "))
    
    elements = []
    print("Input Elements:")
    
    for i in range(n):
        element = int(input())
        elements.append(element)
    
    prime_numbers = ListPrime(elements)
    
    total = sum(prime_numbers)
    prime_output = "+".join(map(str, prime_numbers))
    print(f"Output: {total} ({prime_output})")

def main():
    sum_of_prime_elements()

if __name__ == "__main__":
    main()