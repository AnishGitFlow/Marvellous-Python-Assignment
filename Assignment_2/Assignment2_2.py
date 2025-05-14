def pattern(n):
    for i in range(n):
        print('* ' * n)

def main():
        n = int(input("Enter a number: "))       
        if n <= 0:
            print("Please enter a positive number.")
            return           
        pattern(n)

if __name__ == "__main__":
    main()