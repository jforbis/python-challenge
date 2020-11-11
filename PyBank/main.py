#importing my modules so I can reference my file path and file that I'm going to read.
import os
import csv

# Specifying how to find my file.
csvpath = os.path.join('Resources','budget_data.csv')

# Specifying how to open and read the file.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    listrows = list(csvreader)
    print(listrows)
    
    date = []
    profit_loss = []
    avg_change = []

    for row in csvreader:
        #grab date and store it in 'date' list
        date.append(row[0])
        #grab floater value from profit_loss and store in list
        profit_loss.append(row[1])
        change = 
        
    #print outputs
    print("Financial Analysis")
    print("----------------------------")
    #calculate number of months
    print("Total Months: ", len(date))
    #this for loop is saying, 'for every row in the column of profit loss, change each value to an integer'
    for i in range(0,len(profit_loss)):
        profit_loss[i] = int(profit_loss[i])
        
    #declare 'x' variable and calculate profit_loss column in file (should equal 38,382,578)
    x = sum(profit_loss)
    #print(f"Total: " + '${:.2f}'.format(x)) - SAVE FOR LATER WHEN DOING AVERAGE CHANGE
    print(f"Total: $" + str(x))
    #declare 'y' variable and calculate average change (add everything up then divide by row count)
    #calculation to get amount changed from row to row
    print(profit_loss(row[i])-profit_loss(row[i-1]))
                
    y = (sum(profit_loss)/len(profit_loss))
    #Greatest increase in profits (list month and amount)
    #greatest decrease in profits (list month and amount)


# fileoutput = os.path.join("budget_analysis"
# with open(fileoutput, "w", newline=" ") as datafile:
#   writer = csv.writer(datafile)
#   writer.writerow(...list out data column headers...)
#   writer.writerows(...variable for your zipped list...)