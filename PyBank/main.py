#importing my modules so I can reference my file path and file that I'm going to read.
import os
import csv

# Specifying how to find my file.
csvpath = os.path.join('Resources','budget_data.csv')

# Specifying how to open and read the file.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    #listrows = list(csvreader)
    #print(listrows)
    
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
        
    #declare 'x' variable and calculate profit_loss column in file (should equal 38,382,578)
    x = sum(profit_loss)
    #print(f"Total: " + '${:.2f}'.format(x)) - SAVE FOR LATER WHEN DOING AVERAGE CHANGE
    print(f"Total: $" + str(x))
    #declare 'y' variable and calculate average change (add everything up then divide by row count)
    #calculation to get amount changed from row to row
    average_changes = []

    for j in range(1,len(profit_loss)):
        change = (profit_loss[j])-(profit_loss[j-1])
        average_changes.append(change)
    
    avg_rate_change = (sum(average_changes))/len(average_changes)
    print(f"Average Change: " + '${:.2f}'.format(avg_rate_change))
    
    #Greatest increase in profits (list month and amount)
    max_change = max(average_changes)
    #use 'zip' to pull in the corresponding date info
    print(f"Greatest Increase in Profits: " + '${:.2f}'.format(max_change))
    #print(f"Greatest Increase in Profits: {max_change})
    #greatest decrease in profits (list month and amount)
    min_change = min(average_changes)
    print(f"Greatest Decrease in Profits: " + '${:.2f}'.format(min_change))


# fileoutput = os.path.join("budget_analysis"
# with open(fileoutput, "w", newline=" ") as datafile:
#   writer = csv.writer(datafile)
#   writer.writerow(...list out data column headers...)
#   writer.writerows(...variable for your zipped list...)