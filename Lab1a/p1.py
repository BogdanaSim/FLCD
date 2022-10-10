# verify if a number is prime
if __name__ == '__main__':
    n = int(input("Enter a number: "))
    is_prime = True
    if n <= 1:
        is_prime = False
    if n % 2 == 0 and n != 2:
        is_prime = False
    d = 3
    while d * d <= n:
        if n % d == 0:
            is_prime = False
        d += 2
    if is_prime:
        print("The number %d is prime!" % n)
    else:
        print("The number %d is not prime!" % n)
