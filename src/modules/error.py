def user_correct_input(prompt):
     while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError as e:
            print("Not a valid input! Try again")