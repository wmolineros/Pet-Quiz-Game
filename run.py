
#Start of the quiz with a welcome message 
print("Welcome to the Pet Quiz Game!")
print("This game helps you find out what type of pet best suits your lifestyle.")

def game_contents():
    """
    The player will select either 'yes' or 'no' for a series of questions. 
    Depending on how many of either at the end, the game will suggest the best type
    of pet for the person's lifestyle. The player will be able to select play, discontinue, 
    restart, or advice for first time pet owners. 
    """
print("\n")
print("Press 1-4 to choose from below options:")
print("1. Play \n2. Discontinue \n3. Restart \n4. Advice for first time pet owners. ")

while True:
    game_option = input("How would you like to proceed?\n").strip()
    print(\n)

    if game_option is == "1":
        print("Let's keep moving!\n")
        break 
    elif game_option is == "2":
        print("Reconsidered a life long friend? Sayonara!\n")
        quit()
    elif game_option is == "3":
        print("Let's begin again!\n")
        restart_game()
    elif game_option is == "4":
        display_advice()
        game_option()
    else:
        print("This option is not valid. Please select between option 1-4.")

def player_name():
    """
    Request that the player provide their name
    """
    print("Provide your chosen name.")
    print("Include this in characters A-Z or a-z.")
    print("Do not input any numbers.")
    print("Maximum of 10 characters.")
    print("Blank spaces will be removed.")

    player_name = input("Please enter your  name: \n")

    if verify_player_name(player_name):
        print(\n)
        print(f"Aloha {player_name}, let's begin the quiz game!\n")
        print(f"I see you're an animal lover and would like to")
        print("choose the best pet for your lifestyle, {player_name}!\n")
        print("Type in Y/N, y/n or yes or no to answer each question.\n")
        print("Can't wait to see your result!")
        game_menu()
    
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
    except ValueError:
        print("Oops! There was no valid entry. Please try again.")

    return True

def display_advice:
    print("Before getting a pet, large or small, make sure you're being")
    print("honest with yourself about your lifestyle. You must ask ")
    print("yourself important questions that will allow you to make ")
    print("an informed decision.\n")
    print("For instance, if you have a demanding job, busy social life,")
    print("or not home often enough, opt for a pet that is not very")
    print("demanding or requires a lot of maintenance. Pets to consider")
    print("include house plants, fish, rock. You want to think about the")
    print("well being of the pet you're brining into your home and ask")
    print("yourself if you would be able to enhance their life; not deplete it")





    
