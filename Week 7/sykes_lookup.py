while True: 
  choice = input("Would you like to use the lookup tool? Enter (y) for Yes or (n) for No: ")
  if choice == 'y':
    f = open('address.txt', 'r')
    for line in f:
      fileList = line.strip().lower().split(',')
      data = {}
      data['Name'] = fileList[0]
      data['Street'] = fileList[1]
      data['City'] = fileList[2]
      data['State'] = fileList[3]
      data['Zip Code'] = fileList[4]
      data['Phone'] = fileList[5]
      name = input("Please enter a name: ")
      if name in data:
        print(data)
  # else:
  #   print('You have chosen to quit the program')



