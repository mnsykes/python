def dictLookup():
  f = open('address.txt', 'r')
  for line in f:
    personalInfo = line.lower().strip().split(', ')
    for value in personalInfo:
      myDict = {}
      myDict[personalInfo[0]] = personalInfo[1:]
    for key in myDict:
      print(key, myDict[key])
    # print(myDict)
    

choice = input('Would you like to use the lookup tool? Enter (y) for Yes or (n) for No: ').lower()
if choice == 'y':
  dictLookup()
  
  
  
  


