#Author: Elise Merrifield
#CIS 131
#Extra Cedit Assignment: Target Heart-Rate Calculator
#Code a module that takes input from user and calculates the users maximum heart rate and target range

age = int(input("Please enter your age in years: "))

max_hr = 220 - age
target_hr_trange = round(max_hr*0.85)
target_hr_brange = round(max_hr*0.5)

print("Thank you!")
print(f"Your maximum safe heart rate is: {max_hr} \nand your target range for exercise is: {target_hr_brange}-{target_hr_trange}.")
