def display_board(available_options):
    """
    Display a tic tac toe board on the screen

    :return: board

    """

    print(" ", available_options[1], "|", available_options[2], "|", available_options[3])
    print("-", "-", "-", "-", "-","-", "-")
    print(" ", available_options[4], "|", available_options[5], "|", available_options[6])
    print("-", "-", "-", "-", "-", "-", "-")
    print(" ", available_options[7], "|", available_options[8], "|", available_options[9])
    # print("-", "-", "-", "-", "-", "-")


def get_user_choice(player, valid_choice_list):
    """
    This function displays all choices to the players

    :return:

    """

    valid_choice = False

    while not valid_choice:
        player_choice = input(f"{player} please enter the position where you want to place your choice: "
                              f"{valid_choice_list} : ")
        if player_choice.isdigit():
            if int(player_choice) in valid_choice_list:
                valid_choice = True
                return player_choice
            else:
                print(f"{player} sorry this is not a valid choice, the number has to be between {valid_choice_list} :")
                continue
        else:
            print(f"{player} sorry this is not a valid choice, the number has to be between {valid_choice_list} :")
            continue


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
    user_response = input(message)

    if user_response.upper() == "Y":
        return True
    elif user_response.upper() == "N":
        return False


def is_winning(filled_dict):

    # check row#1
    if (filled_dict[1] == filled_dict[2]) and (filled_dict[2] == filled_dict[3]) \
            and (filled_dict[1] != " " and filled_dict[2] != " " and filled_dict[3] != " "):
        return True

    # check row#2
    if (filled_dict[4] == filled_dict[5]) and (filled_dict[5] == filled_dict[6]) \
            and (filled_dict[4] != " " and filled_dict[5] != " " and filled_dict[6] != " "):
        return True

    # check row#3
    if (filled_dict[7] == filled_dict[8]) and (filled_dict[8] == filled_dict[9]) \
            and (filled_dict[7] != " " and filled_dict[8] != " " and filled_dict[9] != " "):
        return True

    # check column#1
    if (filled_dict[1] == filled_dict[4]) and (filled_dict[4] == filled_dict[7]) \
            and (filled_dict[1] != " " and filled_dict[4] != " " and filled_dict[7] != " "):
        return True

    # check column#2
    if (filled_dict[2] == filled_dict[5]) and (filled_dict[5] == filled_dict[8]) \
            and (filled_dict[2] != " " and filled_dict[5] != " " and filled_dict[8] != " "):
        return True

    # check column#3
    if (filled_dict[3] == filled_dict[6]) and (filled_dict[6] == filled_dict[9]) \
            and (filled_dict[3] != " " and filled_dict[6] != " " and filled_dict[9] != " "):
        return True

    # check diagonal#1
    if (filled_dict[1] == filled_dict[5]) and (filled_dict[5] == filled_dict[9])\
            and (filled_dict[1] != " " and filled_dict[5] != " " and filled_dict[9] != " "):
        return True

    # check diagonal#2
    if (filled_dict[3] == filled_dict[5]) and (filled_dict[5] == filled_dict[7]) \
            and (filled_dict[3] != " " and filled_dict[5] != " " and filled_dict[7] != " "):
        return True

    return False


def get_valid_choice_list(options_dict):

    valid_list_keys = list()

    for key, value in options_dict.items():
        if value == " ":
            valid_list_keys.append(key)
        else:
            continue

    return valid_list_keys


def play_tic_tac_toe_game():

    available_options = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    user_continue = True
    count = 1

    while user_continue:

        display_board(available_options)

        if user_wants_to_continue():
            player_turn = whose_turn_is_it(count)

            # get the available values which has not been chosen by user
            valid_choice_list = get_valid_choice_list(available_options)
            # get user choice
            user_choice = int(get_user_choice(player_turn,valid_choice_list))
            # update the user choice in
            update_available_options(count, available_options, user_choice)
            if is_winning(available_options):
                display_board(available_options)
                print("Congratulations " + player_turn + " won the game ! ")
                user_continue = False
            else:
                count += 1
                continue
        else:
            user_continue = False


play_tic_tac_toe_game()
