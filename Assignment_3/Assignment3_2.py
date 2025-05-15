def find_max_element():
    n = int(input("Input: Number of elements: "))
    
    elements = []
    print("Input Elements:")
    
    for i in range(n):
        element = int(input())
        elements.append(element)
    
    maximum = max(elements)
    print(f"Output: {maximum}")

def main():
    find_max_element()

if __name__ == "__main__":
    main()