import random


def choice_conversion(choice):
    """

    :param choice:
    :return:
    """

    if choice == 1:
        return "Rock"
    if choice == 2:
        return "Paper"
    if choice == 3:
        return "Scissor"


def get_valid_game_option():
    """

    :return:
    """

    user_choice = ""
    valid_choice = False
    game_option = "Choose one of the Option : Rock , Paper or Scissor : "

    while not valid_choice:
        user_choice = input(game_option)
        if user_choice.capitalize() == "Rock" or \
                user_choice.capitalize() == "Paper" or \
                user_choice.capitalize() == "Scissor":
            valid_choice = True
        else:
            msg_invalid_choice = f"This {user_choice} is not a valid choice. "
            print(msg_invalid_choice)
            valid_choice = False
            continue

    return user_choice


def check_user_wants_to_continue():
    """

    :return:
    """
    user_choice = ""
    valid_choice = False
    user_message = "Do you want to continue to play Y / N :"
    msg_invalid_choice = f"This {user_choice} is not a valid choice. "

    while not valid_choice:

        user_choice = input(user_message)
        print("User Choice = ",user_choice)
        if user_choice.upper() == "Y":
            valid_choice = True
            return True
        elif user_choice.upper() == "N":
            valid_choice = False
            return False
        else:
            print(msg_invalid_choice)
            user_choice = input(user_message)
            valid_choice = False
            continue


def play_rock_paper_scissor_game():
    """
    Paper eats rocks ,
    Rock eats scissor,
    Scissor eat Paper,

    :return:
    """

    options_tup = ("Rock", "Paper", "Scissor")
    player_points = 0
    computer_points = 0

    player_wants_to_continue = check_user_wants_to_continue()
    print(player_wants_to_continue)

    while player_wants_to_continue:
        player_option = get_valid_game_option()
        computer_option_num = random.randint(1, 3)
        computer_option = choice_conversion(computer_option_num)
        if player_option in options_tup:
            if player_option == computer_option:
                print(f"It is a tie as you have chosen {player_option} and computer have chosen {computer_option}")
            else:

                # Paper eats rock
                if player_option == "Paper" and computer_option == "Rock":
                    player_points += 1
                    print(f"You win 1 point as you have chosen {player_option} "
                          f"and computer have chosen {computer_option} ")
                elif player_option == "Rock" and computer_option == "Paper":
                    print(f"You lose 1 point as you have chosen {player_option} "
                          f"and computer have chosen {computer_option}")
                    computer_points += 1

                # Rock eats Scissor
                if player_option == "Rock" and computer_option == "Scissor":
                    player_points += 1
                    print(f"You win 1 point as you have chosen {player_option} "
                          f"and computer have chosen {computer_option} ")
                elif player_option == "Scissor" and computer_option == "Rock":
                    print(f"You lose 1 point as you have chosen {player_option} "
                          f"and computer have chosen {computer_option}")
                    computer_points += 1

                # Scissor eats Paper
                if player_option == "Scissor" and computer_option == "Paper":
                    player_points += 1
                    print(f"You win 1 point as you have chosen {player_option} "
                          f"and computer have chosen {computer_option} ")
                elif player_option == "Paper" and computer_option == "Scissor":
                    print(f"You lose 1 point as you have chosen {player_option} "
                          f"and computer have chosen {computer_option}")
                    computer_points += 1
        player_wants_to_continue = check_user_wants_to_continue()

    if player_points > 0 or computer_points > 0:
        if player_points > computer_points:
            print(f"\n Congratulations!!! You WON , Your points are {player_points} "
                  f"and computer points are {computer_points}")
        else:
            print(f"\n Sorry!!! You Lose , Your points are {player_points} "
                  f"and computer points are {computer_points}")
            print(f"\n Better luck next time !!")


play_rock_paper_scissor_game()
