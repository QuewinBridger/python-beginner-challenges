def is_number_of_xs_equal_to_os(word):
  word_as_list_and_lower = list(word.lower())
  count_o = 0
  count_x = 0
  for word in word_as_list_and_lower:
    if word == 'x':
      count_x += 1
    elif word =='o':
      count_o += 1
  
  return check_if_counts_equal(count_x, count_o)

def check_if_counts_equal(count_x,count_o):
  if count_x == count_o:
    return True
  return False

word = 'xxxooo'
print(is_number_of_xs_equal_to_os(word))