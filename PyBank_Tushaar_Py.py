# Import all the dependencies, libraries and modules
import pandas as pd
import numpy
import os
import csv
import sys

#----------------------------------------------------------------------------------------------------------

# Store the source file path to a variable
print("Please make sure that your input files are present in the raw_data folder")
Input_File_Data_Path = os.path.join("..", "raw_data", input ("Please enter the input filename: \n"))

#----------------------------------------------------------------------------------------------------------

# Create new lists for storing the new formatted data for our new output excel file (to be generated)

Date = []
Revenue = []
Revenue_Change = []
Total_Months = 0
Total_Revenue = 0
Revenue_Change_Total = 0
Counter = 0
i=0

# All variables have been defined
#----------------------------------------------------------------------------------------------------------

# Open the CSV

with open(Input_File_Data_Path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csvreader, None)
    
    for row in csvreader: #start parsing through the file
        
        Date.append(row[0]) # write all the dates in the Date column list
        Revenue.append(row[1]) # write all the revenues for each month in the Revenue column list
        
        # This will add the sums of all the revenue entries in the spreadhsheet
        Total_Revenue = Total_Revenue + float(row[1]) 
        Total_Months = len(Date) # Return total number of months in the input file
        

#----------------------------------------------------------------------------------------------------------

# We have read all the values from the CSV, so now we will resume our normal operations in the code

# Calculating the Revenue Change Column Values. These values will be used for further calculations
for i in range(Total_Months-1):
    Revenue_Change.append(float(Revenue[i+1]) - float (Revenue [i]))

# Calculating the maximum Revenue Change
Max_Revenue_Change = max(Revenue_Change)

# Calculating the minimum Revenue Change
Min_Revenue_Change = min(Revenue_Change)

# Calculating the revenue change length - This will be used for calculating the 'average' revenue change
Revenue_Change_len = len(Revenue_Change)

# Calculating the revenue change total - This will be used for calculating the 'average' revenue change
for i in range (Revenue_Change_len):
    Revenue_Change_Total = Revenue_Change_Total + Revenue_Change [i]


# Calculating the average revenue change
Average_Revenue_Change = Revenue_Change_Total/Revenue_Change_len
    
# Calculating the Date for the Minimum Revenue Change   
for i in range (Revenue_Change_len):
    if (Revenue_Change[i] == Min_Revenue_Change):
        Min_Revenue_Change_Date = Date[i+1]

# Calculating the Date for the Maximum Revenue Change
for i in range (Revenue_Change_len):
    if (Revenue_Change[i] == Max_Revenue_Change):
        Max_Revenue_Change_Date = Date[i+1]
        

# All calculations are complete

#----------------------------------------------------------------------------------------------------------


# Now printing the output in the desired format as specified in the homework

print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: "+ str(Total_Months))
print ("Total Revenue: "+ "$" + str(Total_Revenue))
print ("Average Revenue Change: " + "$" + str(Average_Revenue_Change))
print ("Greatest Increase in Revenue: " + str(Max_Revenue_Change_Date) + "  $"+ str(Max_Revenue_Change))
print ("Greatest Decrease in Revenue: " + str(Min_Revenue_Change_Date) + "  $"+ str(Min_Revenue_Change))

#----------------------------------------------------------------------------------------------------------

# Printing the output of the results of our Spreadsheet to a text file - Output_Results.txt
# Creating a file Output_Results.txt in write mode and writing all the data

temp = sys.stdout                 # store original stdout object for later
sys.stdout = open('Output_Results.txt', 'w') # redirect all prints to this output file

print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: "+ str(Total_Months))
print ("Total Revenue: "+ "$" + str(Total_Revenue))
print ("Average Revenue Change: " + "$" + str(Average_Revenue_Change))
print ("Greatest Increase in Revenue: " + str(Max_Revenue_Change_Date) + "  $"+ str(Max_Revenue_Change))
print ("Greatest Decrease in Revenue: " + str(Min_Revenue_Change_Date) + "  $"+ str(Min_Revenue_Change))
print ("Have a great day!")

sys.stdout.close()                # ordinary file object
sys.stdout = temp                 # restore print commands to interactive prompt
print("End of the program! Have a great day!")           # this shows up in the interactive prompt

#----------------------------------------------------------------------------------------------------------





