import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    voter_ID = []
    County = []
    Candidate = []

    for row in csvreader:
        voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

    votes = len(voter_ID)
    khan = 
    correy = 




    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: " + str(votes))

    #x = zip(voter_ID, County, Candidate)
    #y = list(x)
    #print(y)