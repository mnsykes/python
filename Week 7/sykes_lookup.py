
def dictLookup():
  try:
    lookup = {}
    f = open(choice, 'r')
    for line in f:
      personalInfo = line.lower().strip().split(', ')
      lookup[personalInfo[0]] = personalInfo[1:]
    return lookup

  except FileNotFoundError:
    print('Error: file did not open')
if __name__== "_dictLookup_":
  dictLookup()


choice = input('Enter a file to open: ').lower()
print('\n')
lookup = dictLookup()
for key in lookup:
  key = input('Enter a name: ').lower()
  if key in lookup:
    print(lookup[key])
  
  
  
  
  


