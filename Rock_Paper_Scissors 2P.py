import random

CHOICES = ['rock', "paper", "scissors"]

play = True

while play:
    while True:
        player1_choice = str(input("Player One choose what do you want to play (Rock, Paper, Scissors) "))
        player2_choice = str(input("Player Two choose what do you want to play (Rock, Paper, Scissors) "))
        if player1_choice.lower() not in CHOICES:
            print("Choose a correct option")
        elif player1_choice.lower() in CHOICES:
            break 
    player1_points = 0
    player2_points = 0
    print("P1 chose "+ player1_choice)
    print("P2 chose "+ player2_choice)
    if player1_choice == player2_choice:
        print("A tie!")
    elif player1_choice == 'rock' and player2_choice == 'paper':
        print("P2 won!")
        player2_points += 1
    elif player1_choice == 'scissors' and player2_choice == 'rock':
        print("P2 won!")
        player2_points += 1
    elif player1_choice == 'paper' and player2_choice == 'scissors':
        print("P2 won!")
        player2_points += 1
    elif player1_choice == 'rock' and player2_choice == 'scissors':
        print("P1 won")
        player1_points += 1
    elif player1_choice == 'paper' and player2_choice == 'rock':
        print("P1 won!")
        player1_points += 1
    elif player1_choice == 'scissors' and player2_choice == 'paper':
        print("P1 won!")
        player1_points += 1
    player1_choice = ''
    player2_choice = ''
    again=str(input("Do you want to play again, type anything to continue or no to stop "))
    if again == "no":
      play = False
      print("The game has ended. Player One won "+str(player1_points)+" times, and Player Two won "+str(player2_points)+" times")
      print("Thanks for playing, hope you enjoyed it!")
