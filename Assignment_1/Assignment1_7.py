# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

# Input : 8     Output : False
# Input : 25     Output : True

def divisible(number):
    return number % 5 == 0

print(divisible(8))  
print(divisible(25))
