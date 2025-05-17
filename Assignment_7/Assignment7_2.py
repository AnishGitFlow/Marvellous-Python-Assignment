def main():
    numbers = list(map(int, input("Enter list: ").split()))
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"Doubled list: {doubled}")

if __name__ == "__main__":
    main()