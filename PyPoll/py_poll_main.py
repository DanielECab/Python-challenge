#Importing the csv and os and losaing the files using path.join.

import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

#Setting up the variables to track the poll results.

total_votes = 0
candidates = []
candidate_votes = {}
winners_count = 0
winner = ""

#Setting up the reader for the csv and skipping the header row.

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
   
    #Loop for the dataset.

    for row in reader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1

        candidate_votes[candidate] = candidate_votes[candidate] +1


#Printing the output for the txt file.

with open(file_to_output, "w") as txt_file:
    election_header = (
        f"Election Results \n"
        f"------------------ \n"
        f"Total Votes: {total_votes} \n"
        f"------------------ \n"
    )
    txt_file.write(election_header)

#Loop for finding which candidate wins.

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if(votes > winners_count):
            winners_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)

#Winner of the election.
    winner_output = (
        f"--------------\n"
        f"Winner: {winner} \n"
        f"---------------\n" )
    print(winner_output)
    txt_file.write(winner_output)
