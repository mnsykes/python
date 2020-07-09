import sys

  

"""
Function requests user to enter a file to be read and converts that file into a 
dictionary.  Try/except used to catch to display error message if file fails 
to load.
"""
def dictLookup():
  chooseFile = input('To begin using the tool, please enter a file to open: ').lower()
  try:
    lookup = {}
    f = open(chooseFile, 'r')
    for line in f:
      personalInfo = line.lower().strip().split(', ')
      lookup[personalInfo[0]] = personalInfo[1:]

  except FileNotFoundError:
    print('ERROR: FILE NOT FOUND')
    sys.exit(1)

  return lookup

"""
Function with input for user to request phone num or address of a name that they will enter.
If the name is found the function will format the requested information.
"""
def formatInfo():
  lookup = dictLookup()
  for key in lookup:
    while True:
      choice = input('\nEnter (1) to lookup a phone number or (2) for an address: ')
      if not choice:
        print('You have exited the program.')
        sys.exit()
      if choice == '1':
        key = input('\nEnter a space - separated first and last name: ').lower().strip()
        if not key:
          print("You have exited the program.")
          sys.exit()
        if key in lookup:
          newLookup = lookup[key]
          print('Phone number:' + ' ' + newLookup[4])
        if key not in lookup:
          print('Error: Please enter a valid name.')
      elif choice == '2':
        if key in lookup:
          key = input('\nEnter a space - separated first and last name: ').lower().strip()
          if not key: 
            print('You have exited the program.')
            sys.exit()
          newLookup = lookup[key]
          print('Street:' + ' ' + newLookup[0].title())
          print('City:' + ' '   + newLookup[1].title())
          print('State:' + ' '  + newLookup[2].upper())
          print('Zip:' + ' '    + newLookup[3])
        if key not in lookup:
          print('Error: Please enter a valid name.')
      else: 
        if choice != '1' or '2':
          print('Error: Please choose a valid option.')

print('---------------------------------------------------')
print('     ADDRESS AND PHONE NUMBER LOOKUP TOOL          ')
print('---------------------------------------------------')
formatInfo()

# if __name__== "_main_":
#   main()


