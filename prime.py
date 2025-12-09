def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i ==0:
            return False
    return True
n = int(input("Enter a number: "))
if isPrime(n):
    print(f"The number= {n} is a prime")
else:
    print(f"The number= {n} is not a prime")