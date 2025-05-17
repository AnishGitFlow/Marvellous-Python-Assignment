def main():
    numbers = list(map(int, input("Enter 5 numbers: ").split()))
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    print(f"Maximum number is: {max_num}")

if __name__ == "__main__":
    main()