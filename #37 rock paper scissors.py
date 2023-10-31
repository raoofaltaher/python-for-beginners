import random
while True:
    choises =["rock", "paper", "scissors"]

    computer = random.choice(choises)
    player = None

    while player not in choises:
         player = input("rock, paper,or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You Loss!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You WIN!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You Loss!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You WIN!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You Loss!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You WIN!")

    play_again = input("Play again ? (yes/no) ").lower()

    if play_again != "yes":
        break
print("Bye!")