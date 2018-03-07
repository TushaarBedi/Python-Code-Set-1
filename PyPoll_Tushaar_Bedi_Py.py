# Import all the dependencies, libraries and modules
import pandas as pd
import numpy
import os
import csv
import sys

# Ask the user to input the file name
print ("Please make sure your source files are placed in (PyPoll/raw_data folder) ")
Election_Data_Path = os.path.join("..", "raw_data", input ("Please enter the input filename: \n"))

# Read our Data file with the pandas library and store them into their respective data frames
Election_Data_1_df = pd.read_csv(Election_Data_Path, encoding = "ISO-8859-1",low_memory=False)

# Calculating total number of votes from the input spreadsheet
Total_Votes_1 = Election_Data_1_df["Voter ID"].count()

#Finding the unique names of the candidates in Election Data 1 Data Frame
Unique_Candidates_1 = Election_Data_1_df["Candidate"].unique()

# Finding how many votes each candidate has in Election Data 1 Data Frame
Candidate_Voter_Counts_1 = Election_Data_1_df["Candidate"].value_counts()

# Creating a new dataframe with these new values, to summarize the Voter table for Election Data 1 Data Frame
Candidate_Voter_Counts_1_df = pd.DataFrame ({"Candidates": Unique_Candidates_1, "Total Votes": Candidate_Voter_Counts_1})

# Sorting the Candidate Voter Counts Summary Table for Election Data 1 Data Frame
Sort_Voter_Counts_1_df = Candidate_Voter_Counts_1_df.sort_values("Total Votes", ascending = False)

# Adding the percentage coloumn in the new sorted data frame
# Rounding off the percentage to 2 decimal places via using the round function
Sort_Voter_Counts_1_df ["Percentage"] = round(((Sort_Voter_Counts_1_df ["Total Votes"]/Total_Votes_1)* 100), 2)

# Calculating the total candidates in the Sort_Voter_Counts_1 Data Frame
total_candidates_1 = Sort_Voter_Counts_1_df["Candidates"].count()
# The above variable is not being used for now. I have kept them just in case

# Now printing all the election results in the specific format as asked in the homework
# Printing results for Spreadsheet 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_Votes_1))
print("-------------------------")

i = 0
for row in Sort_Voter_Counts_1_df:
    print(str(Sort_Voter_Counts_1_df["Candidates"][i]) +": " + str(Sort_Voter_Counts_1_df["Percentage"][i]) +"% (" +str(Sort_Voter_Counts_1_df["Total Votes"][i])+ ")")
    i = i+1
print(str(Sort_Voter_Counts_1_df["Candidates"][i]) +": " + str(Sort_Voter_Counts_1_df["Percentage"][i]) +"% (" +str(Sort_Voter_Counts_1_df["Total Votes"][i])+ ")")

print("-------------------------")
print("Winner: " + str(Sort_Voter_Counts_1_df["Candidates"][0]))
print("-------------------------")

# Printing the output of the First Spreadsheet to a text file - Output_File_1.txt
# Creating a file Output_First_Spreadsheet.txt in write mode and writing all the data

temp = sys.stdout                 # store original stdout object for later
sys.stdout = open('Output_Results.txt', 'w') # redirect all prints to this output file

# Now printing all the election results in the specific format as asked in the homework
# Printing results for Spreadsheet 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_Votes_1))
print("-------------------------")

i = 0
for row in Sort_Voter_Counts_1_df:
    print(str(Sort_Voter_Counts_1_df["Candidates"][i]) +": " + str(Sort_Voter_Counts_1_df["Percentage"][i]) +"% (" +str(Sort_Voter_Counts_1_df["Total Votes"][i])+ ")")
    i = i+1
print(str(Sort_Voter_Counts_1_df["Candidates"][i]) +": " + str(Sort_Voter_Counts_1_df["Percentage"][i]) +"% (" +str(Sort_Voter_Counts_1_df["Total Votes"][i])+ ")")

print("-------------------------")
print("Winner: " + str(Sort_Voter_Counts_1_df["Candidates"][0]))
print("-------------------------")


sys.stdout.close()                # ordinary file object
sys.stdout = temp                 # restore print commands to interactive prompt
print("Thank you and have a great day!")           # this shows up in the interactive prompt

# End of the program