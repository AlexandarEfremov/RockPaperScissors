import random

r = "rock"
p = "paper"
s = "scissors"

letters = "rps"
print()
player_move = input("Choose rock, paper or scissors - [r/p/s]: ")
print()
computer_move = random.choice(letters)

if player_move == computer_move:
    print("It's a draw!")
elif player_move == "r" and computer_move == "s" or player_move == "p" and computer_move == "r" or player_move == "s" \
        and computer_move == "p":
    if computer_move == "r":
        computer_move = r
    elif computer_move == "p":
        computer_move = p
    else:
        computer_move = s
    print(f"The computer chose {computer_move}.")
    print("You win!")
else:
    if computer_move == "r":
        computer_move = r
    elif computer_move == "p":
        computer_move = p
    else:
        computer_move = s
    print(f"The computer chose {computer_move}.")
    print("You lose.")
