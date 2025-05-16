from functools import reduce

def main():
    input_list = list(map(int, input("Enter numbers separated by space: ").split()))
    
    filtered_list = list(filter(lambda x: x % 2 == 0, input_list))
    print("List after filter =", filtered_list)
    
    mapped_list = list(map(lambda x: x ** 2, filtered_list))
    print("List after map =", mapped_list)
    
    total = reduce(lambda x, y: x + y, mapped_list)
    print("Output of reduce =", total)

if __name__ == "__main__":
    main()