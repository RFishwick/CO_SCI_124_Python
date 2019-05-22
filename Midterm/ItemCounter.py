# Item Counter
# Display number of names stored in the file

def main():
    # Variable definitions
    cnt = 0  # Counter - type integer

    # Open the names.txt file
    infile = open('names.txt', 'r')

    # Read the first name from the file
    name = infile.readline()

    # Continue processing if name is not empty
    while name != '':
        cnt += 1  # Increment counter
        name = infile.readline()  # read next name
        # Return to top of loop

    # Close the file and print the number of names
    infile.close()
    print("Number of names: ", cnt)


# Call the main function
main()
