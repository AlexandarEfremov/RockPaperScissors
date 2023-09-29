import random

r = "rock"
p = "paper"
s = "scissors"


def rock_paper_scissors():
    letters = "rps"
    print()
    player_move = input("Choose rock, paper or scissors - [r/p/s]: ")
    print()
    computer_move = random.choice(letters)

    if player_move == computer_move:
        print("\033[1;33m""It's a draw!""\033[0m")
    elif player_move == "r" and computer_move == "s" or player_move == "p" and computer_move == "r" or player_move == "s" \
            and computer_move == "p":
        if computer_move == "r":
            computer_move = r
        elif computer_move == "p":
            computer_move = p
        else:
            computer_move = s
        print(f"The computer chose {computer_move}.")
        print("\033[0;32m""You win!""\033[0m")
    else:
        if computer_move == "r":
            computer_move = r
        elif computer_move == "p":
            computer_move = p
        else:
            computer_move = s
        print(f"The computer chose {computer_move}.")
        print("\033[0;31m""You lose.""\033[0m")
    while True:
        play = input("Play again? Y/N: ").lower()
        if play == "y":
            rock_paper_scissors()
        elif play == "n":
            exit()
        else:
            print("Wrong input! Try again.")
            continue


rock_paper_scissors()
