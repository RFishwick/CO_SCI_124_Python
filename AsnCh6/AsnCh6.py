# Average of Numbers

def main():
    # Local variables
    counter = 0
    number = 0
    total = 0
    average = 0.0

    try:
        # Open input file
        inputFile = open('numbers.txt', 'r')

        # Read inputFile and total numbers
        for line in inputFile:
            number = int(line)  # Get line from InputFile

            counter += 1
            total += number

        # Close the file
        inputFile.close()

        # Calculate the average
        average = total / counter

        # Display Integer Count and Total Numbers
        print('Integers read:', format(counter, ','))
        print('Total:', format(total, ','))

        # Display the average of all the numbers in the file
        print('Average:', format(average, ',.3f'))

    except IOError:
        print('An error occurred while trying to read the file.')
    except ValueError:
        print('A Non Integer or Non Numeric value found in the file')
    except:
        print('An error occurred')


# Call the main function.
main()


