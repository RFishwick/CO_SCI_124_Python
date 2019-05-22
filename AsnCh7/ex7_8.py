def main():
    # Setup variables
    boy = ''
    girl = ''

    try:
        # Open the file for reading.
        boy_input = open('BoyNames.txt', 'r')

        # Read all the lines in the file into a list.
        popular_boys = boy_input.readlines()

        # Strip trailing '\n' from all elements of the list.
        for i in range(len(popular_boys)):
            popular_boys[i] = popular_boys[i].rstrip('\n')

        # Open the file for reading
        girl_input = open('GirlNames.txt', 'r')

        # Read all the lines in the file into a list.
        popular_girls = girl_input.readlines()

        # Strip trailing '\n' from all elements of the list.
        for i in range(len(popular_girls)):
            popular_girls[i] = popular_girls[i].rstrip('\n')

        # Obtain user input.
        boy = input("Enter a boy's name, or N if you do not" \
                    " wish to enter a boy's name: ")
        girl = input("Enter a girl's name, or N if you do not" \
                     " wish to enter a girl's name: ")

        # Display result for boy's name entered by user
        if boy == 'N':
            print("You chose not to enter a boy's name.")
        elif boy in popular_boys:
            print(boy, "is one of the most popular boy's names.")
        else:
            print(boy, "is not one of the most popular boy's names.")

        # Display result for girl's name entered by user
        if girl == 'N':
            print("You chose not to enter a girl's name.")
        elif girl in popular_girls:
            print(girl, "is one of the most popular girl's names.")
        else:
            print(girl, "is not one of the most popular girl's names.")

    except IOError:
        print("The file could not be found.")
    except IndexError:
        print("There was an indexing error.")
    except:
        print("An error occurred.")


# Call the main function.
main()

