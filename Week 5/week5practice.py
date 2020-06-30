  
"""
Write a program that allows the user to load a file and, repeatedly, display a line of their choice. The
program should:
1. Prompt the user for the name of the file to read/load.
2. The program should read each line of the file into a list (e.g. each element in the list is a
string containing the text of a line in the file)
3. The program should loop indefinitely and
a. Display the number of lines in the file
b. Prompt the user for the line number they would like to see
c. If the line number is 0, exit the program
d. If the line number is non-zero, display the appropriate line of text
e. If the line number is greater than the number of lines in the file, print an error and
continue, asking for another number.
4. Steps 1 & 2 above should be part of a function that prompts the user for the input file, opens
it, reads the file contents into a list and returns the list.
5. Step 3 should be included in a main() function.
Create and run this program as a Python script called lines.py and test it 
"""

import os


file = input("Enter a file name: ")
f = open(file, 'r')
for lineList in f:
    lineList = f.readlines()
    length = len(lineList)
    print("There are" + ' ' + "lines in this file", length)


while True:    
    lineChoice = int(input("What line would you like to print: "))
    if lineChoice == 0:
        break
    elif lineChoice > 6:
        print("Number exceeds number of lines in file. Try again.")
    else:
        lineChoice >= 1 or lineChoice <= 6
        print(lineList[lineChoice])
