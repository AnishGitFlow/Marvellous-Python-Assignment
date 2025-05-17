def main():
    nums = list(map(int, input("Enter three numbers separated by space: ").split()))
    
    if nums[0] >= nums[1]:
        if nums[0] >= nums[2]:
            largest = nums[0]
        else:
            largest = nums[2]
    else:
        if nums[1] >= nums[2]:
            largest = nums[1]
        else:
            largest = nums[2]
    
    print(f"Largest number: {largest}")

if __name__ == "__main__":
    main()