import Arithmetic

def main():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        print(f"Addition: {Arithmetic.Add(num1, num2)}")
        print(f"Subtraction: {Arithmetic.Sub(num1, num2)}")
        print(f"Multiplication: {Arithmetic.Mult(num1, num2)}")
        print(f"Division: {Arithmetic.Div(num1, num2)}")
    
if __name__ == "__main__":
    main()