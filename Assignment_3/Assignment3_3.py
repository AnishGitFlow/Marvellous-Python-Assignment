def find_min_element():
    n = int(input("Input: Number of elements: "))
    
    elements = []
    print("Input Elements:")
    
    for i in range(n):
        element = int(input())
        elements.append(element)
    
    minimum = min(elements)
    print(f"Output: {minimum}")

def main():
    find_min_element()

if __name__ == "__main__":
    main()