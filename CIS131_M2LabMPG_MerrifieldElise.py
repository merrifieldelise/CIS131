'''
Script: Miles per gallon
Action: get user input on gas used and miles driven and average result
Author: Elise Merrifield
Date: 02/01/2026
'''


#initialize variables
miles_total = 0
gallons_total = 0

while True:
    #input for gallons and immediate test for sentinel value
    gallons = float(input("Enter the gallons of gas used (-1 to end): "))

   #start calculation total miles per gallon
    if gallons == -1:
        mpg_total = miles_total / gallons_total #calculate overall MPG
        print(f"The overall average miles/gallon was {mpg_total}")
        break #end loop

    #2nd input for miles driven
    miles = float(input("Enter the miles driven: "))

    #calculate and print trip mgp
    trip_mpg = miles/gallons
    print(f"The miles/gallons for this tank was {trip_mpg}")

    #create totals for calculation
    miles_total += miles
    gallons_total += gallons
