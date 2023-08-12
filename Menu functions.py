# The show_menu function shows menu to user.
# It shows only as many numbers, as many choices are saved inside [options_description].
# Example:
# main_menu = ["Add name.", "Add surname.", "Add age.", "Exit."]
# show_menu(main_menu)
def show_menu(options_description):
    print(
        "Hello! Please select one of the following options:\n"
        "**************************************************"
    )
    for i in range(len(options_description)):
        print(
            f"{i + 1}: {options_description[i]}"
        )
    print(
        "**************************************************"
    )


# Simple way to allow only for a specific input.
# Example: response = ask_yes_no("Enter 'Y' for Yes, 'N' for No: ").
def yes_no_answer(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).upper()
    return response


# Function int_answer_under allow user to input an integer number with value of <= number_of_choice.
# Then it returns correct integer value.
# Example: user_choice = numeric_answer_above(5)
def int_answer_under(number):
    while True:
        try:
            user_input = int(input(
                "Please enter the number: "
            ))
        except ValueError:
            print(
                "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                "It's not a number.\n"
                "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            )
        else:
            if user_input <= number:
                print(
                    f"**************************************************\n"
                    f"Thank you. You choose number: {user_input}.\n"
                    f"**************************************************"
                )
                return user_input
            else:
                print(
                    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                    "Number too high!.\n"
                    f"Highest number is: {number}.\n"
                    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                )


# Function menu_answer takes an options list and shows them as a menu, then collecting an answer from user and
# returns it.
# Example: main_menu = ["Trip calculator", "To-Do list", "Simple game", "Exit"]
# Example: answer_main_menu = menu_answer(main_menu)

def menu_answer(options_description):
    # Show menu:
    print(
        "**************************************************\n"
        "Please select one of the following options:\n"
        "**************************************************\n"
        "0: Exit"
    )
    for i in range(len(options_description)):
        print(
            f"{i + 1}: {options_description[i]}"
        )
    print(
        "0: Exit\n"
        "**************************************************"
    )
    # Return allowed input:
    while True:
        try:
            user_input = int(input(
                "Please enter the number: "
            ))
        except ValueError:
            print(
                "It's not a number.\n"
                "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            )
        else:
            if user_input <= len(options_description) and user_input != 0:
                print(
                    f"**************************************************\n"
                    f"Thank you!\n"
                    f"You choose: {options_description[user_input - 1]}.\n"
                    f"**************************************************"
                )
                return user_input
            elif user_input == 0:
                print(
                    "See you next time!\n"
                    "**************************************************"
                )
                break
            else:
                print(
                    "No functions assigned to this number.\n"
                    f"Highest number is: {len(options_description)}.\n"
                    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                )
