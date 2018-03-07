# Import all the dependencies, libraries and modules
import pandas as pd
import numpy
import os
import csv
import sys

# Store the source file path to a variable
Input_File_Data_Path = os.path.join("..", "raw_data", input ("Please enter the input filename: \n"))


# Create new lists for storing the new formatted data for our new output excel file (to be generated)

Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []


# Creating a data dictionary for the state abbreviations

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# Open the CSV
with open(Input_File_Data_Path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header row
    next(csvreader, None)
    
    for row in csvreader:
        Emp_ID.append(row[0])  #Add Employee ID
        
        #Splitting the Name into independent First Name and Last Name columns, which will later be written to our output CSV file
        new_name = row[1].split(" ") # Name =["Tushaar Bedi"] gets split and stored as new_name = ["Tushaar", "Bedi"]
        First_Name.append(new_name[0]) #Add First Name
        Last_Name.append(new_name[1]) #Add Last Name
        
        # The DOB data will now be re-written into DD/MM/YYYY format by using below function. Tushaar's birthday of 1983-03-13 will be reformated to 13-03-1983
        new_dob = row[2].split ("-") #Splitting the different values in the DOB which are seperated by -. 1983-03-13 will be ["1983", "03, "13"]
        i = new_dob[2] #Storing the dd in a new variable
        new_dob[2] = new_dob[0] #Replacing the last dd by yyyy
        new_dob[0] = i #Replacing the first yyyy to be now dd
        new_join_dob = new_dob # The format of ["13", "03", "1983"] is now stored in a new variable
        new_join_dob = '/'.join(new_join_dob) # The array is joined back to retur the acutal DOB as [13-03-1983]
        DOB.append(new_join_dob) #Writing the whole DOB coloumn to our SSN array, which will be later used to wrte the values to the new csv file
        

             
        # The SSN data should be re-written such that the first five numbers are hidden from view.
        new_ssn = row[3].split("-") # splitting the SSN from 123-456-7890 to ["123", "456", "7890"]
        new_ssn[0] = "***" # Setting first set of three values to *** -> ["***", "456", "7890"]
        new_ssn[1] = "***" # Setting the second set of three values to *** -> ["***", "***", "7890"]
        new_asterix_ssn = new_ssn # Storing this new ["***", "***", "7890"] format to a new variable
        new_asterix_ssn = '-'.join(new_asterix_ssn) #now joining back the SSN to one value with '-' dilimeter inserted, resulting in [***-***-7890] format
        SSN.append(new_asterix_ssn) # Writing the whole SSN column to our SSN array, which will be later used to write the values to the new csv file
        
        # The State data should be re-written as simple two-letter abbreviations
        State.append(us_state_abbrev[row[4]]) #Referencing the two-letter abbreviation from the state abbreviation dictionary defined above, and appending the values to the State array

# Now zipping all my lists together -> Emp_ID, First_Name, Last_Name, DOB, SSN and State
new_formatted_csv = zip(Emp_ID, First_Name, Last_Name, DOB, SSN, State)
print (new_formatted_csv)

# Set variable for output file
output_file = os.path.join("PyBoss_Output.csv")

# Open the output file
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    # Write in zipped rows
    writer.writerows(new_formatted_csv)

# End of the program