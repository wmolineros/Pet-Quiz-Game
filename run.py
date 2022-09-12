
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

yes = True
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