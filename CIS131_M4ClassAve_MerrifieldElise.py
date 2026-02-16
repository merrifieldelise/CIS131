'''
Script: Writing Grades to A Plain Text File
Action: Write a program that enables the user to enter any number of grades
and stores them in a grades.txt plain text file
Author: Elise Merrifield
Date: 02/15/2026
'''

#initialization phase
grade_counter = 0 #number of grades entered

#create and open txt file
with open('grades.txt', mode='w') as grades:
    grade = int(input('Enter grade, -1 to end: '))

#processing phase

    while grade != -1:
        grade_counter += 1 #add to grade counter for each input
        grade = int(input('Enter grade, -1 to end: '))#take input from user and make sentinel value testable
        grades.write(f'{str(grade)} \n')#write input to text file

# print to let user know program has terminated successfully
if grade_counter != 0:
    print(f'{grade_counter} grades were entered and saved!')
else:
    print('No grades were entered.')