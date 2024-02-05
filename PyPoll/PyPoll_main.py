import os
import csv

def analyze_election_data(file_path):
    # Open CSV file
    with open(file_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        # Read the Header row
        header = next(csv_reader)

        # Declare variables
        votes = []
        total_votes = 0
        candidates = {}

        # Start the for loop
        for row in csv_reader:
            # Add the ballot column to the variable
            votes.append(row[0])
            # Count all the votes
            total_votes += 1
            # Create a variable to hold the column names
            candidate_name = row[2]

            # Update votes for each candidate
            if candidate_name not in candidates:
                candidates[candidate_name] = 0
            candidates[candidate_name] += 1

        # Calculate the percentage of votes per candidate
        percentages = {candidate: round((votes / total_votes) * 100, 3) for candidate, votes in candidates.items()}

        # Find the Winner!
        winner = max(percentages, key=percentages.get)

        # Print the results
        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {total_votes}")
        print("-------------------------")
        for candidate, votes in candidates.items():
            print(f"{candidate}: {percentages[candidate]}% ({votes})")
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

        # Output the results as a text file
        output_file_path = os.path.join("Analysis", "PyPoll_output.txt")

        with open(output_file_path, 'w') as textfile:
            # Write the header
            textfile.write("Election Results\n")
            textfile.write("-------------------------\n")
            textfile.write(f"Total Votes: {total_votes}\n")
            textfile.write("-------------------------\n")
            for candidate, votes in candidates.items():
                textfile.write(f"{candidate}: {percentages[candidate]}% ({votes})\n")
            textfile.write("-------------------------\n")
            textfile.write(f"Winner: {winner}\n")
            textfile.write("-------------------------\n")

        print(f"The results have been saved to {output_file_path}")

# Run the analysis
election_data_csv = os.path.join("Resources", "election_data.csv")
analyze_election_data(election_data_csv)