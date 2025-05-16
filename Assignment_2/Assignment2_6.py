def pattern(n):
    for i in range(n, 0, -1):
        print('* ' * i)

def main():
        n = int(input("Enter a number: "))
        if n <= 0:
            print("Please enter a positive number.")
            return
        pattern(n)

if __name__ == "__main__":
    main()