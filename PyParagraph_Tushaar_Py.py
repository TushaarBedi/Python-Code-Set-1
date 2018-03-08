# Import all the dependencies, libraries and modules
import pandas as pd
import numpy
import os
import csv
import sys
import re

# Store the source file path to a variable
print ("Please make sure that the input files are present in the raw_data folder")
Input_File_Data_Path = os.path.join("..", "raw_data", input ("Please enter the input filename: \n"))

# Create new lists for storing the data from the input file (Letters, words, sentences, paragraphs etc.)
Letter = []
Word = []
Sentence = []
Paragraph = []

# Initialize all variables 
Sentence_Length = 0
Letter_Count = 0
Word_Count = 0
Sentence_Count = 0
Paragraph_Count = 0

# Open the text file
with open(Input_File_Data_Path) as txtfile:
    paragraph = txtfile.read()


    Sentence_1 = paragraph.split(".") #Store sentences that are seperated by periods as an array
    Sentence_2 = paragraph.split("!") #Store sentences that are seperated by exclamation marks as an array
    Sentence_3 = paragraph.split("?") #Store sentences that are seperated by question marks as an array
    Word = paragraph.split(" ") #Store all the independent words in the whole text file containing one paragraph as an array
    


Word_Count = len(Word) #get the lenght of the word arrays to calculate approximate independent words
Sentence_Count = len(Sentence_1) - 1 + len(Sentence_2) - 1 + len(Sentence_3) - 1 #Calculate the number of sentences in the paragraph which are seperated by . ! ?
Letter_Count = len (paragraph) #Count all characters in the paragraph. Ideally we should then 'substract' the .,!?""'' etc. In this code we are only returning 'approximates', so we are not writing that code logic
    
Average_Letter_Count = Letter_Count / Word_Count #Simple mathematical formula for average letter count per each word
Average_Sentence_Length = Word_Count/Sentence_Count #Simple mathematical forumula for average sentence length in terms of number of words per sentence

#Printing all the output as desired format specified in the homework

print ("Paragraph Analysis")
print ("-----------------")
print ("Approximate Word Count is: " + str(Word_Count))
print ("Approximate Sentence Count is: " + str(Sentence_Count))
print ("Approximate Letter Count is: " + str (Letter_Count))
print ("Average Letter Count is: "+ str(Average_Letter_Count))
print ("Average Sentence Length is: " + str (Average_Sentence_Length))
           
        
    



        

        
      