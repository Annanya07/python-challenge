import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

DB_Dict = {}
total_votes = 0

#Opening file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        # row[0] is VOTED ID NUM
        # row[1] is County
        # row[2] is Candidate
        if row[2] in DB_Dict.keys():
            if row[1] in DB_Dict[row[2]].keys():
                DB_Dict[row[2]][row[1]] += 1
            else:
                DB_Dict[row[2]][row[1]] = 1
        else:
            DB_Dict[row[2]] = {}
            DB_Dict[row[2]][row[1]] = 1
        total_votes += 1
        
# Get the analysis values

current_max = 0
# Display output
print('Election Results:')
print('-'*25)                                
print('Total votes : {}'.format(total_votes))
print('-'*25)
for candidate in DB_Dict.keys():
    total_per_candidate = 0
    for county in DB_Dict[candidate].keys():
        total_per_candidate += DB_Dict[candidate][county]
    print('{:15s} : {:6.3f}% ({} votes)'.format(candidate, total_per_candidate/total_votes * 100, total_per_candidate))
    if total_per_candidate > current_max:
        leader = candidate
        current_max = total_per_candidate
print('-'*25)
print ('Winner is {}'.format(leader))