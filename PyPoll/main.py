#PyPoll Script
#Process to identify our file (data set)
import os
import csv

# Relative Path using 'Resources' Folder, 'filename'
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the file
with open(csvpath) as csvfile:

# Reads the file using CSV reader function and specifying delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
#Avoid Headers
    next(csvreader, None)
# Set and initialize Total Votes
    total = []
    khan = 0
    correy = 0
    li = 0
    tooley = 0

# Start to analyze data for each row in the file
    for row in csvreader:

# Total Votes
        votes =  row[0]
        total.append(votes)
#Votes for khan
        if row[2] == "Khan":
            khan = int(khan + 1)
        if row[2] == "Correy":
            correy = int(correy + 1)
        if row[2] == "Li":
            li = int(li + 1)
        if row[2] == "O'Tooley":
            tooley = int(tooley + 1)

#Precentages by candidate
    khan_percent = "{:.2%}".format((khan / len(total)))
    correy_percent = "{:.2%}".format((correy / len(total)))
    li_percent = "{:.2%}".format((li / len(total)))
    tooley_percent = "{:.2%}".format((tooley / len(total)))

#Identify Winner
    if khan > correy and khan > li and khan > tooley:
        winner = "Khan"
    elif correy > khan and correy > li and correy > tooley:
        winner = "Correy"
    elif li > khan and li > correy and li > tooley:
        winner = "Li"
    elif tooley > khan and tooley > correy and tooley > li:
        winner = "Tooley"
    else:
        winner = "There is a tie, please review results to declare the winner"

#Print Results to Terminal
    print(f"Election Results")
    print(f"-------------------------------")
    print(f"Total Votes: {len(total)}")
    print(f"-------------------------------")
    print(f"Khan: {khan_percent} ({khan})")
    print(f"Correy: {correy_percent} ({correy})")
    print(f"Li:  {li_percent} ({li})")
    print(f"O'Tooley:  {tooley_percent} ({tooley})")
    print(f"-------------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------------")

#Print results to file
results = (
    "Election Results" "\n"
    "-------------------------------" "\n"
    "Total Votes: " +str(len(total)) + "\n"
    "-------------------------------" "\n"
    "Khan: " + str(khan_percent) + " ("+str(khan)+")" + "\n"
    "Correy: " + str(correy_percent) + " ("+str(correy)+")" + "\n"
    "Li: " + str(li_percent) + " (" +str(li)+")" + "\n"
    "O'Tooley: " + str(tooley_percent) + " (" +str(tooley) + ")"+ "\n"
    "-------------------------------" "\n"
    "Winner: " + str(winner) + "\n"
    "-------------------------------"
)

#Export file
#Set Path for Output and name .txt flile
txtpath = os.path.join('Analysis','pypoll.txt')

#Write txt file
txtfile= open(txtpath, 'w')
txtfile.write(results)
