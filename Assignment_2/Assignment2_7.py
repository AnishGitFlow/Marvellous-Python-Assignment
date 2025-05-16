def pattern(n):
    for i in range(n):
        row = ' '.join(str(j) for j in range(1, n + 1))
        print(row)

def main():
        n = int(input("Enter a number: "))
        if n <= 0:
            print("Please enter a positive number.")
            return
        pattern(n)

if __name__ == "__main__":
    main()