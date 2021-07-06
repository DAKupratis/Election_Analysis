#I'm starting a new file here because it's incredibly unclear to me what code you actually want me to use, and then refer back to old lines of code long after we've created new ones below.
#If anyone from the course actually goes and reads this, I have files on files full of every note and command we've been over so far in this chapter. Let me know if you want to see it.


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
        # Print each row in the CSV file.
    #VVVVV I GUESS WE'RE NOT DOING THIS ANYMORE?????
    #for row in file_reader:
        #print(row)
