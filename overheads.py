#import Path from the built-in module, pathlib
from pathlib import Path
#import the built-in module, csv
import csv

#create a function, overheads_function() with a parameter, forex
def overheads_function(forex):
    #provide a description of the function, overheads_function(forex) using docstring
    """
    The program finds and returns the highest overhead category and its value.
    One parameter is required: forex, which will be the value of SGD for each dollar of USD.
    """
    #create a file path using Path.cwd() to locate the Overheads csv file and assign it to a variable, file_path
    file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
    #open the Overheads csv file in read mode using a with statement, to read its contents
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        #create a reader object to read the csv file using .reader() method 
        reader = csv.reader(file)
        #skip the header in csv file using the next() function
        next(reader)
        #create an empty list, and assign it to the variable 'expenses' 
        expenses = []
        #create a for loop to retrieve the data from the reader object
        for line in reader:
            #append all the overhead values to the empty list, 'expenses' using append() function
            #use the float() function to convert the overhead values from a string to a float
            expenses.append(float(line[1]))
    #open the Overheads csv file again (as it closed previously) in read mode using a with statement, to read its contents
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        #create a reader object to read the csv file using .reader() method
        reader = csv.reader(file)
        #skip the header in csv file using next() function
        next(reader)  
        #create a for loop to retrieve the data from the reader object 
        for line2 in reader:
            #create if statement and set condition as value line2[1] == highest overhead value 
            #use the float() function to convert the overhead values from a string to a float
            if float(line2[1]) == max(expenses):
                #if condition is met, it will return the following f-string using return keyword
                #use the (value difference * forex) equation to convert USD to SGD, and round off the value to 2 decimal place using round() function
                return(f"[HIGHEST OVERHEAD] {line2[0]}: SGD{round(float(line2[1])*forex,2)}\n")
