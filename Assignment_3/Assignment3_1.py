def sum_all_elements():
    n = int(input("Input: Number of elements: "))
    
    elements = []
    print("Input Elements:")
    
    for i in range(n):
        element = int(input())
        elements.append(element)
    
    total = sum(elements)
    print(f"Output: {total}")

def main():
    sum_all_elements()

if __name__ == "__main__":
    main()