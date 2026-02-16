'''
Script: Telephone Number Word Generator
Action: Take user phone Number and use it to generate letter combinations possible
Author: Elise Merrifield
Date: 02/09/2026
Edits: 02/15/2026
'''


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
outputs = []
phone_number = input("Enter your phone number in this format(***-****), avoid using 1's and 0's: ")
#clean input if needed
phone_number = phone_number.replace("-", '')

# Extract each digit's letter group
g0 = letters_numbers[phone_number[0]]
g1 = letters_numbers[phone_number[1]]
g2 = letters_numbers[phone_number[2]]
g3 = letters_numbers[phone_number[3]]
g4 = letters_numbers[phone_number[4]]
g5 = letters_numbers[phone_number[5]]
g6 = letters_numbers[phone_number[6]]

print("Here are all the possible combinations:")

for a in g0:
    for b in g1:
        for c in g2:
            for d in g3:
                for e in g4:
                    for f in g5:
                        for g in g6:
                           outputs.append(a + b + c + d + e + f + g)
                           with open('NumberToLetters.txt', mode='w') as NumberToLetters:
                               for combo in outputs:
                                   NumberToLetters.write(combo + '\n')
                                   print(a + b + c + d + e + f + g)
