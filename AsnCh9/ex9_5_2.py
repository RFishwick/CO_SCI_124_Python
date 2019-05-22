# Write a program that reads the contents of a text file.
# The program should create a dictionary in which the keys are the individual words
# found in the file and the values are the number of times each word appears.
#
# For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the'
# as the key and 128 as the value. The program should either display the frequency of each word
# or create a second file containing a list of each word and its frequency.
#

def main():
    input_name = 'text.txt'  # Assign file name

    # Open the input file and read the text.
    input_file = open(input_name, 'r')  # Open the file for read access
    text = input_file.read()  # Read the file into a string variable
    text = text.strip(',')

    words = text.split()  # Split text into a list of words

    word_count = {}
    for word in words:
        word_count[word] += 1


    # words.sort()
    # print('words: ', words, '/n')
    #
    # #  Create a set of the unique words.
    # unique_words = set(words)
    #
    # print('Unique: ', unique_words, '\n')
    #
    # #  Create a word_count dictionary from unique words and initialize counts to zero
    # word_count = {}
    # for word in unique_words:
    #     word_count[word] = 0
    #
    # # Increment word_count dictionary value for each word in words
    # for word in words:
    #     word_count[word] += 1
    #
    # # Print the results
    print('\n*** Word Frequency ***\n')
    for key in word_count:
        print(key, word_count[key])

    # Close the file.
    input_file.close()


# Call the main function.
main()
