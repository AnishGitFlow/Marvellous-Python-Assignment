# Has a function to display the length of a given name

def DisplayLength(string):
    length = len(string)
    return length

def main():
    name = "Marvellous"
    length = DisplayLength(name)
    print(f"Input: {name}")
    print(f"Output: {length}")

if __name__ == "__main__":
    main()