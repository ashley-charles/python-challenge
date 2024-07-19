import os
import csv
election_csv = os.path.join(r"C:\Users\ashle\python-challenge\PyPoll\Resources\election_data.csv")

Total_Votes = 0
Candidates = {}

Winner = ""
Max_Votes = 0



with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    Votes = list(csvreader)
    Total_Votes = len(Votes) - 1

print("Election Results")
print("----------------------")

print("Total Votes: %d" % Total_Votes)
print("----------------------")

Candidates = {}
for row in Votes[1:]:
    if row[2] not in Candidates:
        Candidates[row[2]] = 1

    else:
        Candidates[row[2]] += 1

for Candidates, vote_count in Candidates.items():
    percentage = (vote_count / Total_Votes) * 100
    print(f'{Candidates}: {percentage: .3f}% ({vote_count})')

    if vote_count > Max_Votes:
        Max_Votes = vote_count
        Winner = Candidates

print("----------------------")


print(f"Winner: {Winner}")

print("----------------------")


    
with open("output.txt", "w") as f:
    print("Election Results", file=f)
    print("----------------------", file=f)
    print("Total Votes: %d" % Total_Votes, file=f)
    print("----------------------", file=f)
    print(f'{Candidates}: {percentage: .3f}% ({vote_count})', file=f)
    print("----------------------", file=f)
    print(f"Winner: {Winner}", file=f)