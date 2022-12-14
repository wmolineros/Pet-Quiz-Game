from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import quizgame


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Pet_Game_Score')


# Start of the quiz with a welcome message
print("Welcome to the Pet Quiz Game!")
print("This game helps you find out what type of")
print("pet best suits your lifestyle.")


def game_contents():
    """
    The player will select either 'yes' or 'no' for a series of statements.
    Depending on how many of either at the end, the game will suggest the
    best type of pet for the person's lifestyle. The player will be able to
    select play, discontinue, restart, or advice for first time pet owners.
    """
    print("\n")
    print("Press 1-4 to choose from below options:")
    print("1. Play \n2. Discontinue \n3. Restart \n4. Advice and scores")

    while True:
        game_option = input("How would you like to proceed?\n").strip()
        print("Type one number from 1-4.\n")

        if game_option == "1":
            print("Let's keep moving!\n")
            break
        elif game_option == "2":
            print("Reconsidered a life long friend? No problem. Sayonara!\n")
            quit()
        elif game_option == "3":
            print("Let's begin again!\n")
            restart_game()
        elif game_option == "4":
            advice_and_score()
        else:
            print("This option is not valid. Please select between")
            print("option 1-4.")


def player_name():
    """
    Request that the player provide their name
    """
    while True:
        print("Provide your chosen name.")
        print("Include this in characters A-Z or a-z.")
        print("Do not input any numbers.")
        print("Maximum of 10 characters.")
        print("Blank spaces will be removed.")

        now = datetime.now()

        datetime_string = now.strftime("%m/%d/%Y %H:%M:%S")

        player_name = input("Please enter your name: \n")

        if verify_player_name(player_name):
            print("\n")
            print(f"Aloha {player_name}, let's begin the quiz game!\n")
            print("I see you're an animal lover and would like to")
            print(f"choose the best pet for your lifestyle, {player_name}!\n")
            print("Type in Y/N or y/n to answer each statement.\n")
            print("Can't wait to see your result!")
            data = quizgame.play_game()
            game_contents()

    verify_player_name(player_name)
    return player_name().strip


def verify_player_name(player_name):
    """
    Ensure that the user's name follows all the necessary criteria.
    A value error will be raised if it is over 10 characters long, no name
    entered or contains any numbers.
    """
    try:
        if not player_name:
            raise ValueError("Please enter a valid player name.")
        if len(player_name) > 10:
            raise ValueError("Player name is too long.")
        if not player_name.isalpha():
            raise ValueError("Only include letters.")
    except ValueError as e:
        print("Oops! That was not a valid entry. Please try again.")
        return False

    return True


def restart_game():
    """
    This section allows the player to play the game multiple times
    """
    while True:
        data = quizgame.play_game()
        now = datetime.now()
        daytime_string = now.strftime("%m/%d/%Y %H:%M:%S")
        score_sheet = SHEET.workshet("score")
        score_sheet.append_row([data, " ", daytime_string])
        game_option()


def advice_and_score():
    """
    This is the advice that is displayed for anyone looking to get more
    information on becoming a pet parent and scores collected.
    """
    while True:
        print("Before getting a pet, large or small, make sure you're being")
        print("honest with yourself about your lifestyle. You must ask ")
        print("yourself important questions that will allow you to make ")
        print("an informed decision.\n")
        print("For instance, if you have a demanding job, busy social life,")
        print("or not home often enough, opt for a pet that is not very")
        print("demanding or requires a lot of maintenance. Pets to consider")
        print("include house plants, fish, rock. You want to think about the")
        print("well being of the pet you're brining into your home and ask")
        print("yourself if you would be able to enhance their life;")
        print("not deplete it.\n")
        print("Throughout this game, you will notice that depending on your")
        print("response for each statement you will receive a suggestion for")
        print("the type of animal (low or high maintenance) that you should")
        print("get.\n Low maintenance pets include a cat, plant fish, hamster")
        print("or small bird.\n")
        print("A high maintenance pet, score of 6 and higher, includes a dog,")
        print("horse, rabbit or large")
        print("birds. A low maintenance pet, scores of below 6, include a cat")
        print("plant or fish.")
        break

    score_details = SHEET.worksheet("Score").get_all_values()[1:]

    for data_info in score_details:
        data_info[0] = int(data_info[0])

    collected_data = sorted(score_details, reverse=True)

    print("All scores recorded.\n")
    print("Line \tScore \tName \t Time")

    for line in range(5):
        print(str(line+1) + "\t" + str(collected_data[line]))


def main():
    """
    This main feature runs all functions for the game.
    """
    game_contents()
    player_name()

main()