# Importing my modules so I can reference my file path and file that I'm going to read.
import os
import csv

# Specifying how to find my file.
csvpath = os.path.join('Resources','budget_data.csv')

# Specifying how to open and read the file.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    # Creating my first two lists to hold the original csv data.
    date = []
    profit_loss = []

    # For loop to go through original data and store values to lists specified above.
    for row in csvreader:
        # Grab date and store it in 'date' list
        date.append(row[0])
        # Grab floater value from profit_loss and store in list
        profit_loss.append(row[1])
        
    # Print outputs
    print("Financial Analysis")
    print("----------------------------")
    
    # Calculate number of months
    print("Total Months: ", len(date))
    
    # This for loop is saying, 'for every row in the column of profit loss, change each value to an integer'
    for i in range(0,len(profit_loss)):
        profit_loss[i] = int(profit_loss[i])
        
    # Declare 'x' variable and calculate profit_loss column in file (should equal 38,382,578)
    x = sum(profit_loss)

    # Printing the total of the profit_loss column
    print(f"Total: $" + str(x))

    # Creating their list to hold values of the changes from month to month from the profit_loss column.
    average_changes = []

    # For loop to go through the profit_loss column and calculate the change from month to month.
    for j in range(1,len(profit_loss)):
        change = (profit_loss[j]) - (profit_loss[j-1])
        average_changes.append(change)
    
    # Zipping my lists together.
    zipper = zip(date,profit_loss,average_changes)
    
    # Variable to hold the zipped data in a list.
    z = list(zipper)
    
    # Variable to calculate the average of "average_changes" column.
    avg_rate_change = (sum(average_changes))/len(average_changes)
    
    # Printing the average of changes for the period.
    print(f"Average Change: " + '${:.2f}'.format(avg_rate_change))
    
    # Greatest increase in profits (list month and amount)
    max_change = max(average_changes)

    # Printing the greatest increase in profit for the period showing the amount and month/year.
    print(f"Greatest Increase in Profits: " + (z[(average_changes.index(max_change))+1][0]) + " " + '${:.2f}'.format(max_change))
    
    # Greatest decrease in profits (list month and amount)
    min_change = min(average_changes)
    
    # Printing the greatest decrease in profit for the period showing the amount and month/year.
    print(f"Greatest Decrease in Profits: " + (z[(average_changes.index(min_change))+1][0]) + " " + '${:.2f}'.format(min_change))

# Taking results and writing them to a new csv file.
output_path = os.path.join("output", "budget_analysis.csv")
with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["Total Months:", len(date)])
    csvwriter.writerow(["Total:", x])
    csvwriter.writerow(["Average Change:", avg_rate_change])
    csvwriter.writerow(["Greatest Increase in Profits:",(z[(average_changes.index(max_change))+1][0]), max_change])
    csvwriter.writerow(["Greatest Decrease in Profits:",(z[(average_changes.index(min_change))+1][0]), min_change])
