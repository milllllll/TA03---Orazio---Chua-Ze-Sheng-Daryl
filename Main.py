#import Path from the built-in module, pathlib
from pathlib import Path
#import the various functions from the api, profit_loss, coh and overhead files
from api import convertUSDtoSGD
from profit_loss import profitloss_function
from cash_on_hand import coh_function
from overheads import overheads_function

#create a file path using Path.cwd() to locate a new file, "Summary Report,txt" and assign it to a variable, summary_filepath
summary_filepath = Path.cwd()/"Summary Report.txt"
#create the new file using .touch() function
summary_filepath.touch()
#execute the convertUSDtoSGD() function and assign the return value to a variable, forex
forex = convertUSDtoSGD()
#open the Summary report txt file in write mode using a with statement, to write content in it
with summary_filepath.open(mode="w", encoding="UTF-8") as info:
    #store the following f-string into a list then write it into the Summary Report txt file using writelines() function
    info.writelines([f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n"])
    #store the return value (highest overhead) of the overheads_function into a list then write it into the Summary Report txt file using writelines() function
    info.writelines([overheads_function(forex)])
    #create a for loop to retrieve data from the return value of 'coh_function()'
    for i in coh_function(forex):
        #store the return value (cash deficit or surplus) of the coh_function into a list then write it into the Summary Report txt file using writelines() function
        info.writelines([i])
    #create a for loop to retrieve data from the return value of 'profitloss_function()'
    for i in profitloss_function(forex):
        #store the return value (profit deficit or net profit surplus) of the profitloss_function into a list then write it into the Summary Report txt file using writelines() function
        info.writelines([i])
