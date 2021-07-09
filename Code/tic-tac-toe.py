def display_board(available_options):
    """
    Display a tic tac toe board on the screen

    :return: board

    """

    print("Available Options in displayBoard", available_options)
    print(available_options[9])
    print(" ", available_options[1], "|", available_options[2], "|", available_options[3])
    print("-", "-", "-", "-", "-","-")
    print(" ", available_options[4], "|", available_options[5], "|", available_options[6])
    print("-", "-", "-", "-", "-", "-")
    print(" ", available_options[7], "|", available_options[8], "|", available_options[9])
    # print("-", "-", "-", "-", "-", "-")


def get_user_choice(player):
    """
    This function displays all choices to the players

    :return:

    """

    valid_choice = False
    is_choice_in_range = False

    while not valid_choice:
        player_choice = input(f"{player} please enter the position where you want to place your choice: '1-9' ")
        is_choice_digit = player_choice.isdigit()
        if is_choice_digit is False:
            print(f"{player} sorry this is not a valid choice")
            continue
        else:
            is_choice_in_range = int(player_choice) in range(1, 10)
            if is_choice_in_range:
                return player_choice
            else:
                print("{player} sorry this is not a valid choice, the number has to be between 1-9")
                continue


# def user_wants_to_continue():
#     return input("Do you like to continue to complete the game (Y/N) : ")


def whose_turn_is_it(counter):

    title = "Player "
    player = ""

    if counter % 2 != 0:
        player = title + "" + str("1")
    else:
        player = title + "" + str("2")

    return player


def update_available_options(count, available_options, user_choice):

    if count % 2 != 0:
        available_options[user_choice] = "X"
    else:
        available_options[user_choice] = "O"


def user_wants_to_continue():

    message = "Do you like to continue to complete the game (Y/N) : "

    if input(message).upper() == "Y":
        return True
    elif input(message).upper() == "N":
        return False
    else:
        print("This is not right option :")
        return user_wants_to_continue()


def play_tic_tac_toe_game():

    available_options = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

    user_choice = None
    user_continue = True
    count = 1

    while user_continue:

        display_board(available_options)

        if user_wants_to_continue():
            player_turn = whose_turn_is_it(count)
            user_choice = int(get_user_choice(player_turn))
            update_available_options(count, available_options, user_choice)
            count += 1
            continue
        else:
            break


play_tic_tac_toe_game()
