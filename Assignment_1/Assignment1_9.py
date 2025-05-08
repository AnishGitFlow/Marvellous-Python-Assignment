# Contains logic to display the first 10 even numbers

def DisplayEvenNumbers():
    count = 0
    number = 2

    while count < 10:
        print(number)
        number = number + 2
        count = count + 1

def main():
    DisplayEvenNumbers()

if __name__ == "__main__":
    main()