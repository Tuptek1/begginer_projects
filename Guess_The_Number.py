import random

play = True
counter = 0
while play:
    number = random.randint(1, 1000)
    while True:
        guess = int(input("Write your guess "))  
        if guess == number:
            print("You guessed right! The number was: "+str(number))
            print("You guessed in: "+str(counter)+" tries")
            counter += 1
            break
        elif guess > number:
            counter += 1
            print("The number you guessed is higher. Try again!")
        elif guess < number:
            counter +=1
            print("The number you guessed is lower. Try again!")
            
    counter = 0
    again=str(input("Do you want to play again, type anything to continue or no to stop "))
    if again == "no":
      play = False
      print("Thanks for playing, hope you enjoyed it!")
