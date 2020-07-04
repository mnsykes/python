def dictLookup():
  data = {}

  with open('address.txt', 'r') as f:
    for line in f:
      fileList = line.strip().lower().split(',')
      key, values = 'name', fileList[0:]
      data[key] = values
      for key in data:
        person = input('Enter a name: ')
        if person in key:
          print(data)
    

choice = input('Would you like to use the lookup tool? Enter (y) for Yes or (n) for No: ').lower()
if choice == 'y':
  dictLookup()



