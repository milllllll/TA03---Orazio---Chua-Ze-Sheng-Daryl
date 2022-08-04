#imort Path from the built-in module, pathlib
from pathlib import Path
#import the built-in module, csv
import csv

#create a function, profitloss_function(), with the parameter, forex
def profitloss_function(forex):
    #provide a description of the function, profitloss_function(forex) using docstring
    """
    The program computes the difference in the net profit between each day and returns
    the days where net profit is lower than the previous day and the value difference.
    One parameter is required: forex, which will be the value of SGD for each dollar of USD.
    """
    #create a file path using Path.cwd() to locate the csv file and assign it to a variable, profit_loss
    profit_loss = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
    #create and empty list and assign to a variable called list_profit
    list_profit = []
    #create and empty list and assign it to a variable called list_day
    list_day = []
    #create and empty list and assign it to a variable called list_overall
    list_overall = []
    #open the Profits and Loss csv file in read mode using a with statement, to read its contents
    with profit_loss.open(mode="r",encoding="UTF-8", newline="") as info:
        #create a reader object
        reader = csv.reader(info)
        #create a for loop to retrieve the data from the reader object
        for line in reader:
            #use try to start the exception handling
            try:
                #append the cash on hand value for each day into the empty list, list_profit, using the append() function
                #use the float() function to convert the net profit value from a string to a float
                list_profit.append(float(line[4]))
                #append the day number into the empty list, list_day, using the append() function
                #use the int() function to convert the day from a string to a integer
                list_day.append(int(line[0]))
            #use except to prevent 'ValueError' from crashing the program, since the headers are strings of words that cannot be converted into a float
            #if detected, it will return to the try statement and the continue keyword helps to repeat the code body again
            except ValueError:
                continue

    for line in reader:
        #append net profits to empty list (list_profit) using append and indexing function
        list_profit.append(int(line[4]))
        #append days to empty list (list_day) using append and indexing function
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

