
def ask_for_int(prompt='Please enter an integer: '):
    while True:
        int_num = input(prompt)
        if int_num.isdigit():
            return int(int_num)
        print("------ please enter valid number  ----")



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

""" the below lines must be run only if this inputs module is run
--> the entry point of the run should be inputs_module.py
"""
print(__name__)
if __name__=='__main__':
    print("""--- Welcome to inputs module ---""")

    print(ask_for_int(prompt='Please enter an integer: '))
    print(ask_for_string(prompt='Please enter a string: '))