# 01 Write a Python program to check that a string contains only a certain set of characters 
# (in this case a-z, A-Z and 0-9)

import re
# indicate set of characters:

characters = '[a-zA-Z]'
digits = '[0-9]'

string_to_search = 'Fsdji47989sdgh*'

def search_string_for_characters():

  string_to_search_replaced = re.sub(characters, '', string_to_search)
  string_to_search_replaced =re.sub(digits,'', string_to_search_replaced)

  if len(string_to_search_replaced) > 0:
    return False
  return True

print(search_string_for_characters())