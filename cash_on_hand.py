#import Path module from pathlib
from pathlib import Path
#import csv module
import csv
#import the exchange rate which is convertUSDtoSGD
from api import convertUSDtoSGD
#create a file path using Path.cwd() and assign it to a variable called coh_path
coh_path = Path.cwd()/"csv_reports"/"cash-on-hand.csv"

#create and empty list and assign to a varibale called list_coh
list_coh = []
#create and empty list and assign it to a variable called list_day
list_day = []
#create a variable name called higher meaning that as the coh each day increased is True
higher = True

#use with keyword to read the coh_path
with coh_path.open(mode="r",encoding="UTF-8", newline="") as info:
    #assign variable called reader to read the csv file 
    reader = csv.reader(info)
    #use next to remove the header from the csv file
    next(reader)
    #create a for loop and assign a variable name for the data in the reader
    for line in reader:
        #append the coh amount for each day to the empty list called list_coh
        list_coh.append(float(line[1]))
        #append the days to the empty list called list_day
        list_day.append(line[0])

    #create a for loop and assign a variable name in the data range of 1 to the number of datas in the list called list_coh
    for i in range(1, len(list_coh)):
        #use if keyword for when the amount in the list_coh decreases from the previous entry
        if list_coh[i] < list_coh[i-1]:
            #print the day the amount decreases from the previous entry and the amount using the conversion rate imported
            print(f"DAY: {list_day[i]}, AMOUNT: SGD{convertUSDtoSGD(list_coh[i])}")
            #assign a variable that higher is False
            higher = False
        #use else keyword to continue to the next iteration if the above is False
        else:
            #use continue keyword to move to the next iteration 
            continue

    #use if keyword and assign if higher equates to True
    if higher == True:
        #print the output saying CASH ON EACH DAY IS HIGHER THEN THE PREVIOUS DAY
        print(f"CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
