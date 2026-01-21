'''
Script: Target Heart-Rate Calculator
Action: takes input from user and calculates the users maximum heart rate and target range
Author: Elise Merrifield
Date: 01/21/2026
'''

#convert input to integer and save as age
age = int(input("Please enter your age in years: "))

#use age to calculate max heart rate
max_hr = 220 - age

#use max_hr to calculate top and bottom of target range
target_hr_trange = round(max_hr*0.85)
target_hr_brange = round(max_hr*0.5)

#Print results
print("Thank you!")
print(f"Your maximum safe heart rate is: {max_hr} "
      f"\nand your target range for exercise is: {target_hr_brange}-{target_hr_trange}.")