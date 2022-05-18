def repeat_the_characters(string):

  new_string = ''
  for i in range(len(string)):
    new_string += string[i]+string[i]

  return new_string

print(repeat_the_characters('now?'))