#importing my modules so I can reference my file path and file that I'm going to read.
import os
import csv

# Specifying how to find my file.
csvpath = os.path.join('Resources','budget_data.csv')

# Specifying how to open and read the file.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
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
    #calculate number of months
    print("Total Months: ", len(date))
    #this for loop is saying, 'for every row in the column of profit loss, change each value to an integer'
    for i in range(0,len(profit_loss)):
        profit_loss[i] = int(profit_loss[i])
    #sum calculation to add profit_loss column in file (should equal 38,382,578)
    print(sum(profit_loss))
    #calculate average change (add everything up then divide by row count)
    #Greatest increase in profits (list month and amount)
    #greatest decrease in profits (list month and amount)


# fileoutput = os.path.join("budget_analysis")
# 
#with open(fileoutput, "w", newline=" ") as datafile:
#   writer = csv.writer(datafile)
#   writer.writerow(...list out data column headers...)
#   writer.writerows(...variable for your zipped list...)uuuuuu