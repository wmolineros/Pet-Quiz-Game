# this is the quiz game section of the game. 

def play_game():
    """
    Throughout this game section, the player will be going through
    each statement and apply an answer to figure out what type of pet 
    they should get depending on their lifestyle. The player will respond 'yes' or 'no'
    to statement and based on these answers, will receive a recommendation."
    """
    score = 0 
    
    # first statement

    while True:
        print("I have a lot of free time. Y/N?\n")
        if response1.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response1.upper() == "N":
            print("Ok, no problem. Something to consider.")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

   # second statement

    while True:
        print("I have a lot of free space. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("That's alright!")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

   # third statement

    while True:
        print("I am looking for companionship. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("No worries!")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")
   
   # fourth statement

    while True:
        print("I have outdoor space. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("Ok, let's see.")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

   # fifth statement

    while True:
        print("I live in the country or suburb. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("Right, no bother!")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

   # sixth statement

    while True:
        print("I am financially stable. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("Ok, no problem. Something to consider.")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

   # seventh statement

    while True:
        print("I like large animals. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("That's alright!")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

   # eight statement

    while True:
        print("Noise is ok with me and my neighbors. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("No worries!")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")
   
   # ninth statement

    while True:
        print("I wish to spend more time outside. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("Ok, let's see.")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")

   # tenth statement

    while True:
        print("I wish to train my pet. Y/N?\n")
        if response2.upper() == "Y":
            print("Closer to your dream pet!\n")
            score += 1
            break
        elif response2.upper() == "N":
            print("Right, no bother!")
            break
        else:
            print("Input is invalid. Please type 'Y' or 'N'.\n")
    
    # The score is tallied up and an answer provided. 
    # The player also gets to see if they're recommended a low or high maintenance pet.

    if score < 6:
        print("A low maintenance pet is best for you; such as a cat or fish.")
        return score
    elif score >= 6:
        print("A high maintence pet would suit your lifestyle perfectly.")
        print("Consider adopting a dog, rabbit, horse or large bird.")
        return score
    else:
        print("It's great to consider a pet. All breeds are fascinating!")
        return score
    



