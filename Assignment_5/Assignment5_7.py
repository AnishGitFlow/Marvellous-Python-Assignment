def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    
    area = length * width
    perimeter = 2 * (length + width)
    
    print(f"Area: {int(area)}")
    print(f"Perimeter: {int(perimeter)}")

if __name__ == "__main__":
    main()