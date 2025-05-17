def main():
    num = int(input("Enter a number: "))
    square = lambda x: x ** 2
    cube = lambda x: x ** 3
    
    print(f"Square: {square(num)}")
    print(f"Cube: {cube(num)}")

if __name__ == "__main__":
    main()