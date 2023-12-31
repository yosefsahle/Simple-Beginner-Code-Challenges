def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if check_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")