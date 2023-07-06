import random

CHOICES = ['rock', "paper", "scissors", "rock solid", "kazdy struga bohatera"]
CHOICES1 = ['rock', "paper", "scissors"]

play = True

while play:
    while True:
        cpu_choice = random.choice(CHOICES1)
        player_choice = str(input("Choose your option (Rock, Paper, Scissors) "))
        if player_choice.lower() not in CHOICES:
            print("Choose a correct option")
        elif player_choice.lower() in CHOICES:
            break 
    player_points = 0
    cpu_points = 0
    print("You chose "+ player_choice)
    print("Computer chose "+ cpu_choice)
    if player_choice == cpu_choice:
        print("A tie!")
    elif player_choice.lower() == "rock solid":
        print("Twardy jak skala")
    elif player_choice.lower() == "kazdy struga bohatera":
        print("dopoki nie przyjmie olowiu w dupe")
    elif player_choice == 'rock' and cpu_choice == 'paper':
        print("U lost!")
        cpu_points += 1
    elif player_choice == 'scissors' and cpu_choice == 'rock':
        print("U lost!")
        cpu_points += 1
    elif player_choice == 'paper' and cpu_choice == 'scissors':
        print("U lost!")
        cpu_points += 1
    elif player_choice == 'rock' and cpu_choice == 'scissors':
        print("U won!")
        player_points += 1
    elif player_choice == 'paper' and cpu_choice == 'rock':
        print("U won!")
        player_points += 1
    elif player_choice == 'scissors' and cpu_choice == 'paper':
        print("U won!")
        player_points += 1
    player_choice = ''
    cpu_choice = ''
    again=str(input("Do you want to play again, type anything to continue or no to stop "))
    if again == "no":
      play = False
      print("The game has ended. You won "+str(player_points)+" times, and the computer won "+str(cpu_points)+" times")
      print("Thanks for playing, hope you enjoyed it!")
