import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidates = []
candidate_votes = {}
winners_count = 0
winner = ""

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1

        candidate_votes[candidate] = candidate_votes[candidate] +1

with open(file_to_output, "w") as txt_file:
    election_header = (
        f"Election Results \n"
        f"------------------ \n"
        f"Total Votes: {total_votes} \n"
        f"------------------ \n"
    )
    txt_file.write(election_header)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if(votes > winners_count):
            winners_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)

    winner_output = (
        f"--------------\n"
        f"Winner: {winner} \n"
        f"---------------\n" )
    print(winner_output)
    txt_file.write(winner_output)
