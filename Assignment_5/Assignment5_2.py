def main():
    char = input("Enter a character: ").lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if char in vowels:
        print(f'"{char}" is a vowel')
    else:
        print(f'"{char}" is a consonant')

if __name__ == "__main__":
    main()