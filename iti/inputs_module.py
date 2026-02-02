


def ask_for_string(prompt :str ='Please enter a string: '):
    """
    this function will ask user to enter a string
    :param prompt: input prompt
    :return:
    """
    while True:
        string_num = input(prompt)
        if string_num.isalpha():
            return string_num
        print("------ please enter valid string  ----")
