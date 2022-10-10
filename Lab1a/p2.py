# compute gcd of 2 numbers
if __name__ == '__main__':
    a, b = map(int, input("Choose two numbers (separated by space): ").split())
    copy_a = a
    copy_b = b
    if a == 0 and b == 0:
        gcd = 0
    elif a == 0:
        gcd = b
    elif b == 0:
        gcd = a
    else:
        r = a % b
        while r:
            a = b
            b = r
            r = a % b
        gcd = b
    print("The gcd of %d and %d is: %d" % (copy_a, copy_b, gcd))
