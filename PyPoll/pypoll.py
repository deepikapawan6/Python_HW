import os
import csv

csv_path = os.path.join(".","Resources","Election_data.csv")
file_to_output = os.path.join("Output","Election_result.txt")
total = 0
list_1 = []
votes = {}
winning_candidate = ""
winning_count = 0

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    
    
    for row in csvreader:
        total += 1
        candidate_name = row[2]
        if candidate_name not in list_1:
            list_1.append(candidate_name)
            
            votes[candidate_name] = 0
        votes[candidate_name] = votes[candidate_name] + 1
        
with open(file_to_output, "w") as txt_file:
    election_results = (
       f"\n\nElection Results\n"
       f"-------------------------\n"
       f"Total Votes: {total}\n"
       f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
    for candidate in votes:
        total_votes = votes.get(candidate)
        votes_percent = float(total_votes)/float(total)*100
        if (total_votes > winning_count):
            winning_count = total_votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {votes_percent:.3f}% ({total_votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
    print(f"-------------------------\n")
        
    winning_candidate_summary = (f"Winner:{winning_candidate}")
    print(winning_candidate_summary)
    print(f"-------------------------\n")
    
    txt_file.write(winning_candidate) 
    



