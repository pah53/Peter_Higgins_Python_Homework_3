import os
import csv

records = os.path.join("03-Python_homework_Instructions_PyPoll_Resources_election_data.csv")

candidate = []
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
vote_totals = []
khan = []
correy = []
li = []
otooley = []


with open(records, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    next(csv_reader)
    for row in csv_reader:
        candidate.append(row[2])
    
    for name in candidate:
        if name == "Khan":
            khan.append(name)

        if name == "Correy":
            correy.append(name)

        if name == "Li":
            li.append(name)

        if name == "O'Tooley":
            otooley.append(name)

    total_votes = len(candidate)
    khan_pct = (len(khan) / total_votes) * 100
    correy_pct = (len(correy) / total_votes) * 100
    li_pct = (len(li) / total_votes) * 100
    otooley_pct = (len(otooley) / total_votes) * 100

    khan_votes = len(khan)
    correy_votes = len(correy)
    li_votes = len(li)
    otooley_votes = len(otooley)

    vote_totals = [khan_votes, correy_votes, li_votes, otooley_votes]

    winner_votes = max(vote_totals)

    print(vote_totals)
    print(winner_votes)

    for item in vote_totals: 
       winner_index = vote_totals.index(winner_votes)
    
    winner_name = candidate_list[winner_index]

print("Election Results")
print("-------------------------------------------")
print(f'Total votes: {total_votes}')
print(f'Khan: {khan_pct}% {khan_votes}')
print(f'Correy: {correy_pct}% {correy_votes}')
print(f'Li: {li_pct}% {li_votes}')
print(f'OTooley: {otooley_pct}% {otooley_votes}')
print(f'Winner: {winner_name} {winner_votes}')