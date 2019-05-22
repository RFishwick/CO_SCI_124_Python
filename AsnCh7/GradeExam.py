#  Grade License Exam

def main():
    # Declare local variables
    correct_answer_list = \
        ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    incorrect_answer_list = []  # List to be populated with any incorrect answers

    i = 0  # Loop Counter
    correct_answer_cnt = 0
    incorrect_answer_cnt = 0

    try:
        # Open the file for reading.
        exam_input = open('Exam_Ans.txt', 'r')

        # Read all the lines in the file into a list.
        exam_answer_list = exam_input.readlines()

        # Strip trailing '\n' from all elements of the list.
        for i in range(20):
            exam_answer_list[i] = exam_answer_list[i].rstrip('\n')
            
        # Compare exam_answer_list to correct_answer_list
        for i in range(20):
            if exam_answer_list[i] == correct_answer_list[i]:
                correct_answer_cnt += 1
            else:
                incorrect_answer_list.append(i+1)
                incorrect_answer_cnt += 1

        # Determine if exam passed or failed
        if correct_answer_cnt > 14:
            print("\nExam Passed")
        else:
            print("\nExam Failed")

        # Print detailed results
        print("Correct Answers: ", correct_answer_cnt)
        print("Incorrect Answers: ", incorrect_answer_cnt)
        if incorrect_answer_cnt > 0:
            print("List of Incorrect Answer Numbers: ", incorrect_answer_list)

    except IOError:
        print("The file could not be found.")
    except IndexError:
        print("There was an indexing error.")
    except:
        print("An error occurred.")


# Call the main function.
main()
