#  A program that reads the file’s contents and determines the following:
#  - The number of uppercase letters in the file
#  - The number of lowercase letters in the file
#  - The number of digits in the file
#  - The number of whitespace characters in the file

def main():
    # Local variables
    uppercase_cnt = 0
    lowercase_cnt = 0
    digit_cnt = 0
    whitespace_cnt = 0

    try:
        # Open file text.txt for reading.
        infile = open('text.txt', 'r')

        # Read data into a list.
        # Each list item is one sentence.
        sentences = infile.readlines()

        print("\nRead text.txt file and analyze characters:")

        #  Loop through lines in file
        for line in sentences:
            #  Loop through characters in lines
            for ch in line:
                if ch.isupper():
                    uppercase_cnt += 1
                elif ch.islower():
                    lowercase_cnt += 1
                elif ch.isdigit():
                    digit_cnt += 1
                elif ch.isspace():
                    whitespace_cnt += 1

        print("Upper Case Characters: ", uppercase_cnt)
        print("Lower Case Characters: ", lowercase_cnt)
        print("Numerical Characters: ", digit_cnt)
        print("Whitespace Characters: ", whitespace_cnt)

        # Close the file.
        infile.close()

    # Handle any errors that may occur.
    except IOError:
        print('There was an error while opening the file.')
    except:
        print('An error occurred.')


# Call the main function.
main()
