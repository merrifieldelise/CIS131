#Author: Elise Merrifield
#CIS 131
#M2 Lab: Miles per gallon
#get user input on gas used and miles driven and average result

#initialize variables
miles_total = 0
gallons_total = 0


while True:
    #input statements
    gallons = float(input("Enter the gallons of gas used (-1 to end): "))
    if gallons == -1:
        mpg_total = miles_total / gallons_total
        print(f"The overall average miles/gallon was {mpg_total}")
        break

    miles = float(input("Enter the miles driven: "))
    #calculate and print trip mgp
    trip_mpg = miles/gallons
    print(f"The miles/gallons for this tank was {trip_mpg}")
    #create totals for next calculation
    miles_total += miles
    gallons_total += gallons


