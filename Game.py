import random

while True:
    
    choices = ["rock" , "paper" , "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock , paper or scissors? : ").lower()

    if player == computer:
        print("computer: " + computer)
        print("player: " + player)
        print("tie")

    elif player == "rock" :
        if computer == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("You won")
        if computer == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("You lost")

    elif player == "scissors" :
        if computer == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("You lost")
        if computer == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("You won")

    elif player == "paper" :
        if computer == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("You lost")
        if computer == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("You won")

    play_again = input("You want to play again? (yes/no) ").lower()
    if play_again !="yes":
        break

print("bye")



