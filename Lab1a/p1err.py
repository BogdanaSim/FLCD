# compute de min of 3 numbers
if __name__ == '__main__':
    1a, b, c = map(int, input("Choose three numbers (separated by space): ").split()) # lexical error
    minimum = c
    if 1a < b and 1a < c:
        minimum = 1a
    elif b < c:
        minimum = b
    print("The minimum between the numbers (%d,%d,%d) is: %d % (1a, b, c, minimum)) # lexical error
