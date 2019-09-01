# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:08:56 2019

@author: Hao Moy
"""
import sys 
import re

#Test case to check for the number of command line arguments
if len(sys.argv)<2:
    print("You must feed the program an input and utput file, in that order.")
    exit()

#Input and output files are grabbed from the command line
    #Input file is readable but not modifiable
    #Output file is writable and if there is none, one will be created (this might be unnecessary due to the check in line 11.    
inputFile = open(sys.argv[0],;'r') 
outputFile = open(sys.argv[1],'w+') 

#Declare dictionary to store word as key and its number of appareances as the value. 
words = {}

#Every line of the input file is read and all '.' are replaced with a blank space. 
#Alternatively, inputFile.read() could have been used, but if the file size is huge, the string could fill our memory up. 
#Afterwards, each line is tokenized by blank spaces and each token is added to the dictionary as a key and its value is updated. 
for line in inputFile.readline(): 
    print("Printing og lines:")
    print(line)
    line = re.sub(".", "\s", line)
    print("Printing lines:")
    print(line)
    for word in re.split("\s", line):
        word = word.lower()
        print("Word:")
        print(word)
        words[word] = words[word] + 1

inputFile.close()

#The dictionary listed and that lis is sorted in alphabetical order. 
#Every key and value is printed into the output document.
for word, occurences in sorted(words.items()): 
    outputFile.write(word + " " + occurences)

outputFile.close()

    
    