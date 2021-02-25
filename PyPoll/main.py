import os
import sys
import csv

eFile = os.path.dirname(__file__) + '\Resources\\election_data.csv'

print(eFile)

def Save_CSVData(sdata):
    oPath = f"{os.path.dirname(__file__)}/analysis"
    if not os.path.exists(oPath):
        os.makedirs(oPath)
    with open(f"{oPath}/Output.txt",'w+') as wFile:
        wFile.write(sdata)


with open(eFile,'r') as eCsv:

    dcsvreader = csv.DictReader(eCsv)


    result = {}
    for row in dcsvreader:
        for column, value in row.items():  
            result.setdefault(column, []).append(value)
    tv = len(result['Voter ID'])
    kVotes = 0
    cVotes = 0
    lVotes = 0
    oVotes = 0
    for i in result['Candidate']:
        if i == "Khan":
            kVotes += 1
        elif i == "Correy":
            cVotes += 1
        elif i == "Li":
            lVotes += 1
        elif i == "O'Tooley":
            oVotes += 1
    winner = ""
    
    if kVotes > cVotes and kVotes > oVotes and kVotes > lVotes:
        winner = "Khan"
    elif cVotes > kVotes and cVotes > oVotes and cVotes > lVotes:
        winner = "Correy"
    elif lVotes > kVotes and lVotes > cVotes and lVotes > oVotes:
        winner = "Li"
    elif oVotes > kVotes and oVotes > cVotes and oVotes > lVotes:
        winner = "O'Tooley"


    rsltdata = f"""
    Election Results
    -------------------------
    Total Votes: {tv}
    -------------------------
    Khan: {round(kVotes/tv * 100,2)}% ({kVotes})
    Correy: {round(cVotes/tv * 100,2)}% ({cVotes})
    Li: {round(lVotes/tv * 100,2)}% ({lVotes})
    O'Tooley: {round(oVotes/tv * 100,2)}% ({oVotes})
    -------------------------
    Winner: {winner}
    -------------------------

    """
    print(rsltdata)
    Save_CSVData(rsltdata)