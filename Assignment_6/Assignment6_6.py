def main():
    rows = int(input("Enter the number of rows: "))
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=' ')
        print()

if __name__ == "__main__":
    main()