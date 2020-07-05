import sys

def dictLookup():
  choice = input('To begin using the tool, please enter a file to open: ').lower()
  try:
    lookup = {}
    f = open(choice, 'r')
    for line in f:
      personalInfo = line.lower().strip().split(', ')
      lookup[personalInfo[0]] = personalInfo[1:]
    return lookup

  except FileNotFoundError:
    print('****************************')
    print('  ERROR: FILE DID NOT OPEN ')
    print('  EXIT CODE: 1              ')
    print('****************************')
if __name__== "_dictLookup_":
  dictLookup()

def formatInfo(choice):
  lookup = dictLookup()
  for key in lookup:
    while True:
      choice = input('\nEnter (1) to lookup a phone number or (2) for an address: ')
      if choice == '1':
        key = input('\nEnter a name: ').lower().strip()
        if key in lookup:
          key = input('\nEnter a name: ').lower().strip()
        if key in lookup:
          newLookup = lookup[key]
          print('Phone number:' + ' ' + newLookup[4])
      elif choice == '2':
        newLookup = lookup[key]
        print('Street:' + ' ' + newLookup[0].title())
        print('City:' + ' '   + newLookup[1].title())
        print('State:' + ' '  + newLookup[2].upper())
        print('Zip:' + ' '    + newLookup[3])
      else: 
        if choice != '1' or '2':
          print('error')
      
def main():
  print('---------------------------------------------------')
  print('ADDRESS AND PHONE NUMBER LOOKUP TOOL')
  print('---------------------------------------------------')
  print(formatInfo())
if __name__=='__main__':
  main()
  


