def main():
    sum_even = 0
    for num in range(1, 101):
        if num % 2 == 0:
            sum_even += num
    print(f"Sum of even numbers between 1 to 100 is: {sum_even}")

if __name__ == "__main__":
    main()