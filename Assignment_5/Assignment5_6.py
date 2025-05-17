def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    
    print(f"Temperature in Fahrenheit: {fahrenheit:.1f}°F")

if __name__ == "__main__":
    main()