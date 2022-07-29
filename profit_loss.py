#import Path
from pathlib import Path
#import csv
import csv
#import convertUSDtoSGD from api file
from api import convertUSDtoSGD
#create path for profit_loss
profit_loss = Path.cwd()/"csv_reports"/"profit-and-loss.csv"

#create empty list for profit
list_profit = []
#create empty list for day
list_day = []
#set variable as True
higher = True
#open profit-and-loss.csv using with statement
with profit_loss.open(mode="r",encoding="UTF-8", newline="") as info:
    #use csv.reader() to read information in csv file and assign to variable reader
    reader = csv.reader(info)
    #skip headers from information read
    next(reader)
    #create For loop 
    for line in reader:
        #append net profits to list_profit
        list_profit.append(int(line[4]))
        #append days to list_day
        list_day.append((line[0]))

#create a For loop that repeat based on the number of sublist in the list_profit list (excluding the first sublist)
for i in range(1, len(list_profit)):
    #create if and else statement
    #set condition (net profit of a day is less than the net profit of the previous day) for if statement
    if list_profit[i] < list_profit[i-1]:
    #if condition is met, print the statement using print function and f-string
    print(f"DAY: {list_day[i]}, AMOUNT: SGD{convertUSDtoSGD(list_profit[i])}")
            #set the variable as False
            higher = False
        #set condition (net profit of a day is greater than the net profit of the previous day) for else statement
        else:
            #use continue keyword to move to the next iteration
            continue
    #create a if statement and set a condition (higher equates to True)
    if higher == True:
        #if condition is met, print the statement using print function and f-string
        print (f"NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

