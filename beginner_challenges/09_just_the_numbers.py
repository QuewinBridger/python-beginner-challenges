random_dataset = ['dfjkhsdgljksgf',55005,'-',1235980,'-','somestringlengthxyz','-',50450,'-', 'jiosdghujio' ,1100304123490]

def grab_numbers(random_dataset):

  just_numbers_list = []
  i = 0

  for i in range(len(random_dataset)):
    if isinstance(random_dataset[i],str) == False:
      just_numbers_list.append(random_dataset[i])

    i+=1

  return just_numbers_list

print(grab_numbers(random_dataset))