
# integer error
def correct_int_input(prompt):
     while True:
        try:
            user_int_input = int(input(prompt))
            return user_int_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()

# string error
def correct_str_input(prompt):
     while True:
        try:
            user_str_input = str(input(prompt))
            return user_str_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()

# input when entering periodic table elements
def correct_element_input(prompt):
     while True:
        try:
            user_element_input = str(input(prompt))
            return user_element_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()


# float error
def correct_float_input(prompt):
     while True:
        try:
            user_float_input = float(input(prompt))
            return user_float_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()


def correct_smile_input(prompt):
     while True:
        try:
            user_smile_input = str(input(prompt)) 
            return user_smile_input
        except ValueError as e:
            print("----> Not a valid input! Please try again <----")
            print()
        except NameError:
            print("----> Not a valid input! Please try again <----")
            print()