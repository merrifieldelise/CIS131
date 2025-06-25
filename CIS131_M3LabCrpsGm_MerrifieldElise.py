#Author: Elise Merrifield
#CIS 131
#M3 Lab Analyzing a game of craps
#take the outlined program in figure 4.2 of chapter 5 in the intro to python textbook and increase play count
#as well as storing wins and losses in a dictionary for further analysis


#simulating the game of craps

import random

def roll_dice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return (die1, die2)

def display_dice(dice):
    die1, die2 = dice
    print(f'player rolled {die1}+{die2}={sum(dice)}')

die_values = roll_dice()
display_dice(die_values)

#initialize my_point to appease the python gods
my_point = 0

#determin game status as well as "point" value
sum_of_dice = sum(die_values)

if sum_of_dice in (7, 11):  #win
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12): #loss
    game_status = 'LOST'
else: #creats point value and continues play
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print("Point is", my_point)

#continue game until win or loss
while game_status == 'CONTINUE':
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)
    if sum_of_dice == my_point:
        game_status = 'WON'
    elif sum_of_dice == 7:
        game_status = 'LOST'

#display win or loss
if game_status == 'WON':
    print('Player has won!')
else:
    print('Player loses.')