import os
import csv

csvpath = os.path.join('PyPoll', 'resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_votes = 0
    candidates = []
    K_votes = 0
    C_votes = 0
    L_votes = 0
    O_votes = 0
    for x in csvreader:
        current = x[0]
        total_votes = total_votes + int(current)
        if x[2] == "Khan":
            current = x[0]
            K_votes += int(current)
        if x[2] == "Correy":
            current = x[0]
            C_votes += int(current)
        if x[2] == "Li":
            current = x[0]
            L_votes += int(current)
        if x[2] == "O'Tooley":
            current = x[0]
            O_votes += int(current)    

        if x[2] not in candidates:
            candidates.append(x[2])

    K_per = K_votes/total_votes*100
    C_per = C_votes/total_votes*100
    L_per = L_votes/total_votes*100
    O_per = O_votes/total_votes*100
    
    Winner = []
    current = int(current)
    if current < K_votes:
        current = K_votes
        Winner = "Khan"
    if current < C_votes:
        current = C_votes
        Winner = "Correy"
    if current < L_votes:
        current = L_votes
        Winner = "Li"
    if current < O_votes:
        current = O_votes
        Winner = "O'Tooley"

    print('Total Votes: ',total_votes)
    print('Khan: ',K_per,'% (',K_votes,')')
    print('Correy: ',C_per,'% (',C_votes,')')
    print('Li: ',L_per,'% (',L_votes,')')
    print("O'Tooley: ",O_per,'% (',O_votes,')') 
    print('Winner: ',Winner)
  
    text = [f"Total Votes: {total_votes}", "Khan: {K_per}% ({K_votes})", "Correy: {C_per}({C_votes})", "Li: {L_per}% ({L_votes})", "O'Tooley: {O_per}% ({O_votes})", "Winner: {Winner}"]
    file = open("PollData.txt", "w") 
    file.writelines(text) 
    file.close() 
