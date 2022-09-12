# this is the quiz game section of the game. 

def play_game():
    """
    Throughout this game section, the player will be going through
    each question to figure out what type of pet they should get 
    depending on their lifestyle. The player will respond 'yes' or 'no'
    to questions and based on these answers, will receive a recommendation."
    """
    score = 0 
    
    # first question

    while True:
        print("Do you wish to spend more time outside?")
        response1 = input("Y \nN").strip()
        if response1.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response1.upper() == "N":
            print("Ok, no problem. Something to consider.")
            score -= 1
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

   # second question

    while True:
        print("Do you have outdoor space?")
        response2 = input("Y \nN").strip()
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("Ok, no problem. Something to consider.")
            score -= 1
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

        