from functools import reduce

def main():
    numbers = list(map(int, input("Enter list: ").split()))
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product: {product}")

if __name__ == "__main__":
    main()