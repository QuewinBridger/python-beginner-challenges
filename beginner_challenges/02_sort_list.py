def sort_list(list, order):

  if order == "asc":
    return sorted(list)

  elif order =="dsc":
    return sorted(list,reverse=True)

  return list


list = [1,2,3,4,5,6,8,9,10]
sorted_list = sort_list(list, "asc")
print(sorted_list)