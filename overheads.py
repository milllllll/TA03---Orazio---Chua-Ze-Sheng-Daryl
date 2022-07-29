#import Path
from pathlib import Path
#import csv
import csv
#import convertUSDtoSGD from api file
from api import convertUSDtoSGD
#creating path for overheads
file_path = Path.cwd()/"csv_reports"/"overheads.csv"

#Open csv using with statement 
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    #use csv.reader() to read information in csv file and assign to variable reader
    reader = csv.reader(file)
    #skip headers from information read
    next(reader)
    #create empty list
    expenses = []
    #create a for loop
    for line in reader:
        #append float values to expenses list
        expenses.append(float(line[1]))
    #use sorted() to sort the expenses from lowest to highest
    sorted_expenses = sorted(expenses)

#open overheads.csv using with statement
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    #use csv.reader() to read information in csv file and assign to variable reader
    reader = csv.reader(file)
    #skip headers from information read
    next(reader)  
    #for line2 in reader
    for line2 in reader:
        #Create if statement, to find highest overhead by setting condition (line == highest overhead expense)
        if float(line2[1]) == sorted_expenses[-1]:
            #print highest overhead in SGD using f string
            print(f"{line2[0]}: SGD{convertUSDtoSGD(float(line2[1]))}")