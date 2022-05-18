def primes_finder(integer):
  primes_list=[]
  for i in range(integer+1):
    if i == 0:
      continue

    if i==2:
      primes_list.append(i)
    if i%2 == 0:
      continue
    for j in range(2, int(i**0.5)+1):
      print(j)
      
      if integer%j != 0:
        primes_list.append(i)




  return primes_list

number = 7
print(primes_finder(number))