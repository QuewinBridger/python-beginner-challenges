
def count_vowels_in_string(word):

  list_of_characters=list(word.lower())
  vowel_list = ['a','e', 'i', 'o', 'u']
  vowel_count = 0

  for vowel in vowel_list:

    for character in list_of_characters:
      if character == vowel:
        vowel_count += 1



  return vowel_count

vowel_count =count_vowels_in_string("AAA")
print(vowel_count)