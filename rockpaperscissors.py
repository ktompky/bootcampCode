import random

print("Welcome to the kitty cat dome of doom!!! \n....................\nPlay a game of purrrrfect game of rock paper scissors and defeat King Kitty!")
player1 = input("Enter Player 1's choice: ")
kittycat = random.choice(["rock","paper","scissors"])

print("Let the games begin!")
print("Player 1 chose " + player1 + "!!")
print("Kitty chose " + kittycat + "!!")

if player1 == kittycat:
    print("What will King Kitty do, it's a tie??!!!")
elif player1 == "rock":
    if kittycat == "scissors":
        print("Player 1 wins!")
    elif kittycat == "paper":
        print("King Kitty wins!")
elif player1 == "paper":
    if kittycat == "scissors":
        print("King Kitty wins!")
    elif kittycat == "rock":
        print("Player 1 wins!")
elif player1 == "scissors":
    if kittycat == "rock":
        print("King Kitty wins!")
    elif kittycat == "paper":
        print("Player 1 wins!")



