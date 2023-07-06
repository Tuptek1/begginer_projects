import random

player_score = 0
cpu_score = 0
play = True

while play:
    while True:
        start = input("Press 'Enter' to roll the dice!")
        cpu_num = random.randint(1, 6)
        player_num = random.randint(1, 6)
        
        print("You rolled a "+ str(player_num))
        print("Computer rolled a "+ str(cpu_num))
        
        cpu_score += cpu_num
        player_score += player_num
        
        if cpu_num == 1:
            cpu_score = 0
            print("Computer rolled a 1 so his counter is getting reseted!")
        
        if player_score == 1:
            player_score = 0
            print("You rolled a 1 so your counter is getting reseted!")    
        
        elif cpu_score >= 30:
            win_condition = 1
            print("The computer won!")
            break
        
        elif player_score >= 30: 
            win_condition = 2
            print("You won!")
            break
        
        print("########################################")
        print("Player score: "+str(player_score))
        print("Computer score: "+str(cpu_score))
        print("########################################")
    cpu_score = 0
    player_score = 0
    again=str(input("Do you want to play again, type anything to continue or no to stop "))
    if again == "no":
        play = False
        if win_condition == 1:
            print("The game has ended. Computer won!!")
        if win_condition == 2:
            print("The game has ended. You won!!")
        print("Thanks for playing, hope you enjoyed it!")

            
        
        