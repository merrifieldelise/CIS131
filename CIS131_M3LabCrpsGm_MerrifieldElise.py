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
while counter < 1000000:
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

#calculate totals
total_wins = sum(win_dict.values())
total_losses = sum(loss_dict.values())
total_games = total_wins + total_losses

#overall percentages
pct_wins = (total_wins/total_games)*100
pct_losses = (total_losses/total_games)*100

#prepare per-roll stats
all_rolls = sorted(set(win_dict) | set(loss_dict))
per_roll_counts = {r: win_dict.get(r, 0) + loss_dict.get(r, 0) for r in all_rolls}

#print summary
print(f"Percentage of wins: {pct_wins}%")
print(f"Percentage of losses: {pct_losses}%\n")

#header for per-roll table
print("\t% Resolved\t\t\t\tCumulative %")
print(" Rolls on this roll of games resolved")
print("----------------------------------------")

#initialise variable for table calculations
cumulative = 0.0
#print table
for r in all_rolls:
    count = per_roll_counts[r]
    pct_each = (count / total_games) * 100
    cumulative += pct_each
    print(f"{r:<6} {pct_each:8.2f}%{12*' '}{cumulative:8.2f}%")