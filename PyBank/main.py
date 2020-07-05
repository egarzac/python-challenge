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
    total_months = []
    a = []
    b = []
    c = []
    increase = 0
    decrease = 0
    max_month = ''
    min_month = ''

# Start to analyze data for each row in the file
    for row in csvreader:

# Total Months List
        months =  row[0]
        total_months.append(months)
#Total value
        total += int(row[1])

#MTM Profit/Loss
        profit = int(row[1])
#a list stands for current month P&L
        a.append(profit)
#b list stands for P&L in next month
    b = a.copy()
    del a[-1]
    del b[0]
    #print(a) - to confirm value
    #print(b) - to confirm value
    #List c is the subtraction of P&L month+1 minus previous month (P&L MTM change)
    c = [x1 - x2 for (x1, x2) in zip(b, a)]
    #print(c) - to confirm value

#Average Change
    average = int(sum(c) / len(c))

#Find Greatest increase and Greatest decrease
    increase = max(c)
    decrease = min(c)

#Find month of greatest increase and decrease
#Note use +1 in Month index as P&L change list c is the substraction MTM thus has -1 in index
    max_month = total_months[c.index(increase)+1]
    min_month = total_months[c.index(decrease)+1]

#Print results in console
    print("-------Financial Analysis------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${total}")
    print(f"Average Change: {average}")
    print(f"Greatest Increase in Profits: {max_month} ({increase})")
    print(f"Greatest Decrease in Profits: {min_month} ({decrease})")

#Print results to text file
results = (
    "-------Financial Analysis------" "\n"
    "Total Months: " +str(len(total_months)) + "\n"
    "Total: $" +str(total) + "\n"
    "Average Change: " +str(average) + "\n"
    "Greatest Increase in Profits: " +str(max_month) + " " + "(" +str(increase) + ")" + "\n"
    "Greatest Decrease in Profits: " +str(min_month) + " " + "(" +str(decrease) + ")"
)

#Export file
#Set Path for Output and name .txt flile
txtpath = os.path.join('Analysis','pybank.txt')

#Write txt file
txtfile= open(txtpath, 'w')
txtfile.write(results)
