"""
Program: sykes_phones.py
Author: Matthew Sykes
Date: 6/21/20

This program will search entries in a data file of names and phone numbers
to match user's request 

Input: User will input last name or first and last name 

Output: Full name and phone number will be returned based on input by user.
"""

# Infinite loop to run until user enters blank space in input
while True:

  print('\n')
  # Get input from user, display error message if conditions not met
  name = input('Please enter a last name or a first name and last name: ').lower().split()
  if len(name) > 2:
    print('Error: Please limit input to two names' '\n')

  # Open and read text file
  f = open('phones.txt', 'r')

  # Loop to run through text file and find matches to user input
  for line in f:
    line = line.lower().split()

    # Variables assigned based on number of names entered by user
    if len(name) == 2:
      firstName = name[0]
      lastName = name[1]

      # If match found print results based on first and last name
      if firstName == line[0] and lastName == line[1]:
        print(line[0].title() + ' ' + line[1].title() + ', ' + line[2])
      
    else:
      # If match found print results based on last name only 
      lastName = name[0]
      if lastName in line[1]:
        print(line[0].title() + ' ' + line[1].title() + ', ' + line[2])
          

  
  

  