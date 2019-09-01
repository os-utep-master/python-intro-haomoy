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

print("test passed")

#Input and output files are grabbed from the command line
    #Input file is readable but not modifiable
    #Output file is writable and if there is none, one will be created (this might be unnecessary due to the check in line 11.    
print(sys.argv[1])
print(sys.argv[2])

inputFile = open(sys.argv[1],'r+') 
outputFile = open(sys.argv[2],'w+') 

print("files opened")

#Declare dictionary to store word as key and its number of appareances as the value. 
words = {}

#Read input file as a single string
#Proceed to delete whitespace and split by periods and spaces
#Turn words into lower case 
inputString = inputFile.read()
print(inputString)
inputString = inputString.strip()
print(inputString)
inputWords = re.split('[ \t]', inputString)
print(inputWords)

for word in inputWords: 
    print("Printing words:")
    print(word)
    word = word.lower() 
    print(word)
    if (words[word]):
        words[word] += 1
    else: 
        words[word] = 1 
    print("End for loop")
    
'''
for line in inputLines: 
    print("Printing og lines:")
    print(line)
    line = re.sub(".", "\s", line)
    print("Printing lines:")
    print(line)
    for word in re.split("\s", line):
        word = word.lower()
        print("Word:")
        print(word)
        words[word] += 1
'''
inputFile.close()
print("input closed")
#The dictionary listed and that lis is sorted in alphabetical order. 
#Every key and value is printed into the output document.
for word, occurences in sorted(words.items()): 
    outputFile.write(word + " " + occurences)

outputFile.close()

print("end")
    