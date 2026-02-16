'''
Script: Writing Grades to A Plain Text File
Action: Take any number of grade inputs and calculate class average, save to text file
Author: Elise Merrifield
Date: 02/15/2026
'''


#class average program from fig 3.2
#initialization phase
total = 0 #grade sums
grade_counter = 0 #number of grades entered

#processing phase
grade = int(input('Enter grade, -1 to end: '))
while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))

#termination phase
if grade_counter != 0:
    average = total / grade_counter
    print(f'Class average is {average:.2f}')
    # Write program to a text file
    with open('ClassGradeAve.txt', mode='w') as ClassGradeAve:
        ClassGradeAve.write(str(average))
else:
    print('No grades were entered')

