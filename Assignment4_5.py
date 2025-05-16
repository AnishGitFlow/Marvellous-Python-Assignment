from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    input_list = list(map(int, input("Enter numbers separated by space: ").split()))
    
    filtered_list = list(filter(is_prime, input_list))
    print("List after filter =", filtered_list)
    
    mapped_list = list(map(lambda x: x * 2, filtered_list))
    print("List after map =", mapped_list)
    
    max_num = reduce(lambda x, y: x if x > y else y, mapped_list)
    print("Output of reduce =", max_num)

if __name__ == "__main__":
    main()