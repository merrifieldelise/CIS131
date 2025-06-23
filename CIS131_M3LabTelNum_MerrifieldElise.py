#Author: Elise Merrifield
#CIS 131
#M3 lab Telephone Number Word Generator
#Take user phone Number and use it to generate letter combinations possible

#inport modules
from itertools import product

#create a dictionary to store the number as a key and associate it with its list of letters
letters_numbers = {
    "2":['A', 'B', 'C'],
    "3":['D', 'E', 'F'],
    "4":['G', 'H', 'I'],
    "5":['J', 'K', 'L'],
    "6":['M', 'N', 'O'],
    "7":['P', 'R', 'S'],
    "8":['T', 'U', 'V'],
    "9":['W', 'X', 'Y']
}
#prompt user input
phone_number = input("Enter your phone number in this format(***-****): ")
#clean input if needed
phone_number = phone_number.replace("-", '')

#create a list of possible combinations from the user input
letters_list = [letters_numbers[digit] for digit in phone_number if digit in letters_numbers]

#print results
print("Here are all the possible combinations for your number: ")
for combo in product(*letters_list):
    print(''.join(combo))