def get_test_scores():
    """
    This function assigns a series of test scores to dictionary values, with keys representing the order they were
    entered in
    :return: this returns a dictionary containing values of all test scores entered
    """
    scores_dict = dict()
    num_scores = 0
    invalid_message = "Invalid test score, try again! ("
    index = 0
    while True:  # Assigning number of tests to be input
        try:
            num_scores = int(input("Enter the number of scores being input: "))
            if 0 > num_scores:
                raise ValueError
            break
        except ValueError as err:
            print("Invalid number of tests. Enter again.")

    while index < num_scores:  # Assigning test values to the dictionary
        try:
            score = int(input("Enter the test score: "))
            if 0 <= score <= 100:
                scores_dict.update({index: score})
                index = index + 1
            else:
                raise ValueError
        except ValueError as err:
            print(invalid_message + str(score) + ")")
    return scores_dict


def average_scores(dict_a):
    """
    Converts the values of a dictionary to a list and returns the average of every value in that list
    :param dict_a: dictionary containing a list of test scores and keys regarding order they were entered in
    :return: the average of every value stored in the passed dictionary
    """
    average = 0
    list_a = list(dict_a.values())
    for index in range(len(list_a)):
        average = average + list_a[index]
    average = average / len(list_a)
    return average


if __name__ == '__main__':
    dict_m = get_test_scores()  # {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    avg = average_scores(dict_m)
    print("The average score is: " + avg + "%")


