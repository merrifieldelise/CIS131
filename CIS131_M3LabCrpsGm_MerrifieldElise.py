'''
Script: Analyzing a game of craps
Action: play 1,000,000 games of craps and store results in a win/loss dictionary
Author: Elise Merrifield
Date: 02/09/2026
'''

#import necessary modules
import random

#create functions for rolling dice and displaying dice rolls
def roll_dice():
    die1 = random.randrange(1,6)
    die2 = random.randrange(1,6)
    return die1, die2

def display_dice(dice):
    die1, die2 = dice


#initialize counter so it doesn't reset unless module is run again
counter = 0

#create empty dictionary's for wins and losses
win_dict = {}
loss_dict = {}

#create loop to run game 1,000,000x
while counter < 100:
    # initiate rolls counter and my_point here so it updates each play
    rolls = 1 #starting at one to account for first roll
    my_point = 0
    # run game
    die_values = roll_dice()
    display_dice(die_values)

    #determin game status as well as "point" value
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):  #win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12): #loss
        game_status = 'LOST'
    else: #creats point value and continues play
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    #continue game until win or loss
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        display_dice(die_values)
        rolls += 1
        sum_of_dice = sum(die_values)
        if sum_of_dice == my_point:
            game_status = 'WON'
        elif sum_of_dice == 7:
            game_status = 'LOST'

    #update dictionaries
    if game_status == 'WON':
        win_dict[rolls] = win_dict.get(rolls, 0) + 1
    else:
        loss_dict[rolls] = loss_dict.get(rolls, 0) + 1

    counter += 1 #add to game counter

#create sorted list of keys without overwriting dictionaries
all_keys = sorted(set(win_dict) | set(loss_dict))

#print dictionaries for wins and losses
print("# of Rolls | Wins\t# of Rolls | Losses")
print("_________________\t___________________")
#for loop to print the sorted results
for k in all_keys:
    print(f"{k:9} | {win_dict.get(k,0):4}\t{k:9} | {loss_dict.get(k,0):4}")