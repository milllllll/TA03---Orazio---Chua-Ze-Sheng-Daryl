#import built in function, Path 
from pathlib import Path
#import functions from api, profit_loss, coh and overhead files
from api import convertUSDtoSGD
from profit_loss import profitloss_function
from cash_on_hand import coh_function
from overheads import overheads_function

#set csv summary report to variable, 'summary_filepath' 
summary_filepath = Path.cwd()/"Summary Report.txt"
#create file path using touch() function
summary_filepath.touch()
#create variable, 'forex' to execute the convertUSDtoSGD() function
forex = convertUSDtoSGD()
#open csv file in write mode using with statement
with summary_filepath.open(mode="w", encoding="UTF-8") as info:
    #write the following f-string (real time currency conversion rate) into the summary csv using writelines() function
    #and convert it from string to list using empty list, []
    info.writelines([f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n"])
    #write the highest overheads from overheads file into the summary csv using writelines() function
    #and convert it from string to list using empty list, []
    info.writelines([overheads_function(forex)])
    #create a For loop that repeat based on the function, 'coh_function()'
    for i in coh_function(forex):
        #write cash deficit or surplus (according to the function) into the summary csv using writelines() function
        #and convert it from string to list using empty list, []
        info.writelines([i])
    #create For loop that repeat based on the function, 'profitloss_function()'
    for i in profitloss_function(forex):
        #write profit deficit or net profit surplus (according to the function) into the summary csv using writelines() function
        #and convert it from string to list using empty list, []
        info.writelines([i])