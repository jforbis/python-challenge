#importing my modules so I can reference my file path and file that I'm going to read.
import os
import csv

# Specifying how to find my file.
csvpath = os.path.join('Resources','budget_data.csv')

# Specifying how to open and read the file.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    date = []
    profit_loss = []

    for row in csvreader:
        #grab date and store it in 'date' list
        date.append(row[0])
        #grab floater value from profit_loss and store in list
        profit_loss.append(row[1])
    #print outputs
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", len(date))
    #sum calculation to add profit_loss column in file (should equal 38,382,578)
    total = int(sum(profit_loss))
    print(total)

    #do calculations here on the data 
    #calculate number of months *try count row*
    #calculate total for profit_loss column
    #calculate average change (add everything up then divide by row count)
    #Greatest increase in profits (list month and amount)
    #greatest decrease in profits (list month and amount)


# fileoutput = os.path.join("budget_analysis")
# 
#with open(fileoutput, "w", newline=" ") as datafile:
#   writer = csv.writer(datafile)
#   writer.writerow(...list out data column headers...)
#   writer.writerows(...variable for your zipped list...)