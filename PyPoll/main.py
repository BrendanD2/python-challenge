# Importing necessary packages
import os
import csv

# Creating a path to open the election data. 
csvpath = os.path.join( 'PyPoll','resources', 'election_data.csv')

# Opening the csv file.
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Header of the csv file, commented out because it not needed to be printed in the terminal.
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Setting variables for the total votes, each candidates name, and the number of votes per candidate.
    total = 0
    
    candidate1 = "Charles Casper Stockham"
    candidate1_votes = 0
    
    candidate2 = "Diana DeGette"
    candidate2_votes = 0
    
    candidate3 = "Raymon Anthony Doane"
    candidate3_votes = 0
    
    # Going through each row and finding which candidate the person voted for. Adding 1 to that candidate vote and 1 to the total votes. 
    for row in csvreader:
        total = total + 1
        if row[2] == candidate1:
            candidate1_votes += 1
        elif row[2] == candidate2:
            candidate2_votes += 1
        elif row[2] == candidate3:
            candidate3_votes += 1
    
    # Finding the percentage of votes for each candidate.
    percent1 = (candidate1_votes / total) * 100
    percent2 = (candidate2_votes / total) * 100
    percent3 = (candidate3_votes / total) * 100
    
    # Creating a list of all of the variables found
    election_list = [total, candidate1, candidate1_votes, percent1,
                     candidate2, candidate2_votes, percent2,
                     candidate3, candidate3_votes, percent3]
    
    # Creating a function to print out the results. This function takes in a list.
    def Print_results(myList):
        print(f"Election Results")
        print("-------------------------")
        print(f"Total Votes: {myList[0]}")
        print("-------------------------")
        print(f"{myList[1]}: {myList[3]:.3f}% ({myList[2]})")
        print(f"{myList[4]}: {myList[6]:.3f}% ({myList[5]})")
        print(f"{myList[7]}: {myList[9]:.3f}% ({myList[8]})")
        print("-------------------------")
        print("Winner: " + myList[4])
        print("-------------------------")
        
    # Running the function with the list we created earlier.
    Print_results(election_list)

    # Creating the path to where we are exporting the text file to. 
    output_path = os.path.join('PyPoll','analysis', 'results.txt')
    # Opening the text file and printing the results the same way we did when creating the function. 
    with open(output_path, "w") as resultstxt:
        resultstxt.write(f"Election Results\n"
        "-------------------------\n"
        f"Total Votes: {election_list[0]}\n"
        "-------------------------\n"
        f"{election_list[1]}: {election_list[3]:.3f}% ({election_list[2]})\n"
        f"{election_list[4]}: {election_list[6]:.3f}% ({election_list[5]})\n"
        f"{election_list[7]}: {election_list[9]:.3f}% ({election_list[8]})\n"
        "-------------------------\n"
        f"Winner: {election_list[4]}\n"
        "-------------------------")
    
    