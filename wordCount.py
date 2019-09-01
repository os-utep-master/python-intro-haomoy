# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:08:56 2019

@author: Hao Moy
"""
import sys 
import re

'''
#Used for local testing.
inputPath = 'C:/Users/haomo/Documents/CS/Classes/OS/lab1/python-intro-haomoy/declaration.txt'
outputPath = 'C:/Users/haomo/Documents/CS/Classes/OS/lab1/python-intro-haomoy/output.txt'
inputFile = open(inputFile,'r')
outputFile = open(outputPath, 'w+')
'''

#Test case to check for the number of command line arguments
if len(sys.argv)<2:
    print("You must feed the program an input and utput file, in that order.")
    exit()
    
#Declare dictionary to store word as key and its number of appareances as the value. 
words = {}

#Input file is grabbed from the command line.
#Input file is readable but not modifiable.
#Encased in 'with as' to control the opening, processing, and closing of the file.
with open(sys.argv[1],'r') as inputFile:
    inputString = inputFile.read() #Read input file as a single string
    inputString = inputString.rstrip() #Proceed to delete whitespace and split by periods and spaces
    inputWords = re.split('[^a-zA-Z]', inputString) #Every character that is not alpha will mark the end of a word
    for word in inputWords: 
        word = word.lower() #Turn words into lower case 
        print(word)
        if word: #Check for empty strings
            if words.get(word): #Check if word has been seen before
                words[word] += 1
            else: 
                words[word] = 1

#Output file is grabbed from the command line.
#Input file is readable but not modifiable.
#Encased in 'with as' to control the opening, processing, and closing of the file.
with open(sys.argv[1],'r') as inputFile:
    outputFile = open(sys.argv[2],'w+') 
    #The dictionary is listed and that list is sorted in alphabetical order. 
    #Every key and value is printed into the output document.
    for word, occurences in sorted(words.items()): 
        outputFile.write(word + " " + str(occurences) + "\n")
    
    
    