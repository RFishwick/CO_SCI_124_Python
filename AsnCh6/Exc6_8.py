def main():
    # Local variables
    counter = 0
    total = 0
    number = 0

    # Open input file
    inputFile = open('random_numbers.txt', 'r')

    # Read numbers from the file while keeping count
    # and a running total
    for line in inputFile:
        number = int(line)
        total += number
        counter += 1

    # Close the file
    inputFile.close()

    print('Total:', format(total, ','))
    print(counter, 'numbers were read from the file.')


# Call the main function.
main()


