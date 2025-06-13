#Author: Elise Merrifield
#CIS 131
#M2 Lab: Guess the Number
#game trying to guess randomly generated number

#import random
import random

go_again = True

#set up while loop
while go_again:
    #set number value to be guessed and create counter
    winner = random.randint(1, 1000)
    counter = 0
    while True:
        #set input and print for getting user input
        guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        counter += 1

        if guess > winner:
            print("Too high. Try again.")

        elif guess < winner:
            print("Too low. Try again.")

        else:
            print(f"Congratulations. You guessed the number in {counter} guesses.")
            break
        if counter == 10:
            print("You should be able to do better!")
            print(f"The correct number was {winner}")



    user_input_loop = input("Would you like to go again?(enter Y or N): ")
    if user_input_loop.lower() != "y":
        go_again = False
