# compute the sum of n numbers
if __name__ == '__main__':
    s = 0
    n = int(input("Value of n: "))
    numbers = list(map(int, input("Enter the numbers (separated by space): ").strip().split()[:n]))
    for x in numbers:
        s += x
    print("Sum of the numbers is: ", s)
