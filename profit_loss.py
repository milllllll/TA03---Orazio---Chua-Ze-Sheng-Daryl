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
        #set the variable, 'higher' as True
        higher = True
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
        #create a for loop that repeats the code body based on the number of sublists in list_profit
        #this is excluding the first sublist, since there is no previous day data to compare with
        for i in range(1, len(list_profit)):
            #create if and else statements 
            #set condition (net profit of a day is less than the net profit of the previous day) for the if statement
            if list_profit[i] < list_profit[i-1]:
                #if condition is met, set variable, 'higher' as False
                higher = False
                #append the following f-string into the empty list, 'list_overall' 
                #use the (value difference * forex) equation to convert USD to SGD, and round off the value to 2 decimal place using round() function
                list_overall.append(f"[PROFIT DEFICIT] DAY: {list_day[i]},  AMOUNT: SGD{round((list_profit[i-1]-list_profit[i])*forex,2)}\n")
            #set condition (net profit of a day is greater than the net profit of the previous day) for the else statement
            #if the condition of the if statement is not met, the code body under the else keyword will be ran
            else:
                #use continue keyword to move to the next iteration
                continue
        #create another if statement and set the condition, higher == True
        if higher == True:
            #if the condition is met, append the following f-string to the empty list, list_overall, using append() function
            list_overall.append((f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"))
        #return the 'list_overall' using return keyword
        return list_overall
