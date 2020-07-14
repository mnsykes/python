'''

Program: Guilbeault_lines.py 
Author: Nicholas Guilbeault
Last date modified: 6/27/2020

The purpose of this program is to display requested lines of a file. The program
is a loop that continually asks for a line, runs through lines of the file till
it finds that line and then prints out that line. It will loop until a zero is
given for the requsted line.

'''
# Define functions

# function to open a file and creat a list with the elements of the list being the line of the file
def read_file_to_list(fileName):
    with open(fileName, 'r') as f:
              linesList = f.readlines()
    return linesList

# function to print a line by indexing a list
def find_line(linesList, userInput):
    print(linesList[userInput])



    
# Main function
def main():
    # declare variables, read file into a list, determine the number of lines and print number of lines
    userInput = ''
    fileName = input("Please input file name: ")
    lineslicedlist = read_file_to_list(fileName)
    numoflines = len(lineslicedlist)
    print("There are %d lines in this file." % numoflines)


    # loop asking for input and displaying lines till 0 is entered
    while userInput != '0':
        userInput = input("Please give number of line you wish to display.\nEnter 0 to end program.\n: ")
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput == 0:
                quit()
            elif userInput > numoflines:
                print("You have entered a number greater than the lines in the file.\nPlease enter a number from 1 to %d.\n" % numoflines)
            else:
                print(lineslicedlist[userInput - 1])
        else:
            print("You have entered an invalid input. Please enter a positive numberfrom 1 to %d.\n" % numoflines)
            continue
        

if __name__ == "__main__":
    main()

