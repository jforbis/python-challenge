# Importing dependencies.
import os
import csv
import numpy

# Variable for the path to my csv file that I want to read.
csvpath = os.path.join('Resources', 'election_data.csv')

# Opening my csv file and reading its contents (skipping the header).
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Creating lists so I can reference them and their values later.
    voter_ID = []
    County = []
    Candidate = []

    # For loop to go through the whole file and add each index of every row column to applicable lists created above.
    for row in csvreader:
        voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
    
    # Variable to return total number of voters.    
    votes = len(voter_ID)
    # Variable to return total number of UNIQUE candidates.
    unique = list(numpy.unique(Candidate))

    # Variable to hold the number of votes the candidate in the 0th index of my UNIQUE list received.
    w = Candidate.count(unique[0])
    # Variable to find percentage of total votes received.
    perw = format(round((w/votes)*100),".3f")
    
    # Variable to hold the number of votes the candidate in the 1st index of my UNIQUE list received.    
    x = Candidate.count(unique[1])
    # Variable to find percentage of total votes received.
    perx = format(round((x/votes)*100),".3f")
    
    # Variable to hold the number of votes the candidate in the 2nd index of my UNIQUE list received.
    y = Candidate.count(unique[2])
    # Variable to find percentage of total votes received.    
    pery = format(round((y/votes)*100),".3f")
    
    # Variable to hold the number of votes the candidate in the 3rd index of my UNIQUE list received.
    z = Candidate.count(unique[3])
    # Variable to find percentage of total votes received.
    perz = format(round((z/votes)*100),".3f")

    # Variable to return the winner based on highest vote count and the corresponding index from unique candidate list.
    winner = {w:unique[0],x:unique[1],y:unique[2],z:unique[3]}

    # Printing out election results.
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: " + str(votes))
    print("-------------------------")
    print(f"{unique[0]}: {perw}% ({str(w)})")
    print(f"{unique[1]}: {perx}% ({str(x)})")
    print(f"{unique[2]}: {pery}% ({str(y)})")
    print(f"{unique[3]}: {perz}% ({str(z)})")
    print("-------------------------")
    print(f"Winner: {winner.get(max(winner))}")
    print("-------------------------")

# Taking poll data and writing it to a new csv file.
output_path = os.path.join("output", "poll_data.csv")
with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["Total Votes:",votes])
    csvwriter.writerow([f"{unique[0]}:",f"{perw}%",w])
    csvwriter.writerow([f"{unique[1]}:",f"{perx}%",x])
    csvwriter.writerow([f"{unique[2]}:",f"{pery}%",y])
    csvwriter.writerow([f"{unique[3]}:",f"{perz}%",z])
    csvwriter.writerow(["Winner:",winner.get(max(winner))])