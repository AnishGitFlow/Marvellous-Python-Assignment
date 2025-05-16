def count_element_frequency():
    n = int(input("Input: Number of elements: "))
    
    elements = []
    print("Input Elements:")
    
    for i in range(n):
        element = int(input())
        elements.append(element)
    
    search_element = int(input("Element to search: "))
    
    frequency = elements.count(search_element)
    print(f"Output: {frequency}")

def main():
    count_element_frequency()

if __name__ == "__main__":
    main()