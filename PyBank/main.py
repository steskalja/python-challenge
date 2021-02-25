import os
import sys
import csv

bFile = os.path.dirname(__file__) + '\Resources\\budget_data.csv'

print(bFile)

def Save_CSVData(sdata):
    oPath = f"{os.path.dirname(__file__)}/analysis"
    if not os.path.exists(oPath):
        os.makedirs(oPath)
    with open(f"{oPath}/Output.txt",'w+') as wFile:
        wFile.write(sdata)


with open(bFile,'r') as bCsv:

    dcsvreader = csv.DictReader(bCsv)


    result = {}
    for row in dcsvreader:
        for column, value in row.items():  # consider .iteritems() for Python 2
            result.setdefault(column, []).append(value)
    tm = len(result['Date'])
    vals = []
    for i in result['Profit/Losses']:
        vals.append(int(i))
    tl = sum(vals)
    avgc = round(tl/tm,2)
    vMax = max(vals)
    dMax = result['Date'][vals.index(max(vals))]
    vMin = min(vals)
    dMin = result['Date'][vals.index(min(vals))]
    rsltdata = f"""
    Financial Analysis
    ----------------------------------------------------------------
    Total Months: {tm}
    Total: ${tl}
    Average Change: ${avgc}
    Greatest Increase in Profits: {dMax} (${vMax})
    Greatest Decrease in Profits: {dMin} (${vMin})
    """
    print(rsltdata)
    Save_CSVData(rsltdata)