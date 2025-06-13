#Author: Elise Merrifield
#CIS 131
#M2 Lab: Miles per gallon
#get user input on gas used and miles driven and average result

#initialize variables
miles_total = 0
gallons_total = 0
gallons = 0
miles = 0


while gallons != -1:
    #input statements
    gallons = float(input("Enter the gallons of gas used (-1 to end): "))
    miles = float(input("Enter the miles driven: "))

    miles_total += miles
    gallons_total += gallons

