import os
import csv
import numpy

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
    unique = list(numpy.unique(Candidate))

    w = Candidate.count(unique[0])
    perw = round((w/votes)*100,5)
    
    x = Candidate.count(unique[1])
    perx = round((x/votes)*100,5)
    
    y = Candidate.count(unique[2])
    pery = round((y/votes)*100,5)
    
    z = Candidate.count(unique[3])
    perz = round((z/votes)*100,5)




    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: " + str(votes))
    print("-------------------------")
    print(f"{unique[0]}: " + str(perw) + str(w))
    print(f"{unique[1]}: " + str(perx) + str(x))
    print(f"{unique[2]}: " + str(pery) + str(y))
    print(f"{unique[3]}: " + str(perz) + str(z))
    print("-------------------------")
    print("-------------------------")




    #x = zip(voter_ID, County, Candidate)
    #y = list(x)
    #print(y)