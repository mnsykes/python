"""
Program: sykes_lookup.py
Author: Matthew Sykes
Date: 7/12/20

This program will accept user input of a person's name and will output either the 
person's name or their phone number depending on user's request.  

Inputs: User keys enter to load file and begin program
        User inputs first and last name
        User inputs choice of phone number or address

Ouptuts: Formatted phone number or address

"""

import sys

"""
Main function loads file and calls for returned dictionary from dictLookup function.
Requests user to enter choice of phone number or address.
Calls function formatInfo to format requested information.

"""

def main():
  print('---------------------------------------------------')
  print('     ADDRESS AND PHONE NUMBER LOOKUP TOOL          ')
  print('---------------------------------------------------')

  useLookup = input('\nTo begin using the lookup tool please press Enter...')
  lookup = dictLookup()

  while True:
    choice = input('Enter (1) to look up a phone number or enter (2) to look up an address: ')
    if choice == '1' or choice == '2':
      formatInfo(choice)
    else:
      print('\nPlease choose a valid option\n')
    
  

"""
Function with input for user to request phone numbwe or address of a name that they will enter.
If the name is found the function will format the requested information.  If the name is not 
found an error will be printed and request input of a name.  A blank input from the user
will exit the program.

"""
def formatInfo(choice):
  search = dictLookup()
  for key in search:
    if choice == '1':
      key = input('\nEnter a space - separated first and last name: ').lower().strip()
      if not key:
        print('You have exited the program')
        quit()
      elif key in search:
        newLookup = search[key]
        print('Phone number:' + ' ' + newLookup[4])
      else:
        if key not in search:
          print('Error: Please enter a valid name.')

    elif choice == '2':
      key = input('\nEnter a space - separated first and last name: ').lower().strip()
      if not key:
        print('You have exited the program')
        quit()
      elif key in search:
        newLookup = search[key]
        print('Street:' + ' ' + newLookup[0].title())
        print('City:' + ' '   + newLookup[1].title())
        print('State:' + ' '  + newLookup[2].upper())
        print('Zip:' + ' '    + newLookup[3])
      else:
        if key not in search:
          print('Error: Please enter a valid name.')
      

"""
Function requests user to enter a file to be read and converts that file into a 
dictionary.  Try/except used to catch to display error message if file fails 
to load.

"""
def dictLookup():
    lookup = {}
    try:
        f = open('address.txt', 'r')
        for line in f:
          personalInfo = line.lower().strip().split(',')
          lookup[personalInfo[0]] = personalInfo[1:]

    except FileNotFoundError:
        print('ERROR: FILE NOT FOUND')
        sys.exit(1)

    return lookup


if __name__ == "__main__":
  main()


