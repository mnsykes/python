
choice = input("Y or N:  ")
if choice == 'y':
  data = dict()
  data['name'], data['street'], data['city'], data['state'], data['zip'], data['phone']  = [], [], [], [], [], []
  with open('address.txt', 'r') as f:
    for line in f:
      keyValPairs = line.split(',')
      for kvPair in keyValPairs:
        kv = kvPair.strip().lower().split(':')
        print(kv)
        key = kv[0]
        val = kv[1]
        data[key].append(val)
else:
  print('You have chosen to quit the program')




# , data['street'], data['city'], data['state'], data['zip'], data['phone'] = [], [], [], [], [], []