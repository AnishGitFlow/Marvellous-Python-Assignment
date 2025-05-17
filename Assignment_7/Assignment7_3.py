def main():
    numbers = list(map(int, input("Enter list: ").split()))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")

if __name__ == "__main__":
    main()