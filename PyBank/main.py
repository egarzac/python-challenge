#PyBank Script

#Process to identify our file (data set)
import os
import csv

# Relative Path using 'Resources' Folder, 'filename'
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the file
with open(csvpath) as csvfile:

# Reads the file using CSV reader function and specifying delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
#Avoid Headers
    next(csvreader, None)
# Set and initialize Total
    total = 0
# Create lists for profit or loss for current date (a), date + 1 (b) and their difference (c)
    a = []
    b = []
    c = []

# Start to analyze data for each row in the file
    for row in csvreader:
#Total value
        total += int(row[1])
#MTM Profit/Loss
        profit = int(row[1])
        a.append(profit)
    b = a.copy()
    del a[-1]
    del b[0]
    #print(a) - to confirm value
    #print(b) - to confirm value
    c = [x1 - x2 for (x1, x2) in zip(b, a)]
    #print(c) - to confirm value

#Average Change
    average = int(sum(c) / len(c))

#Print results
    print(f"Total: {total}")
    print(f"Average Change: {average}")
