def count_digits(n):
    n_str = str(abs(n))
    return len(n_str)

def main():
        n = int(input("Enter a number: "))
        result = count_digits(n)
        print(result)

if __name__ == "__main__":
    main()