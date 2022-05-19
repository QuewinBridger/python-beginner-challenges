# https://www.codecademy.com/code-challenges/code-challenge-find-xth-number-in-order-python

# Find the Xth Number In Order
# Write a function, getX, that given an integer x and a list nums returns the Xth number if the list was in sorted order. In other words, the Xth smallest number.

# Function Name: getX

# Input: An integer, x, and an unsorted list of integers nums that aren’t necessarily distinct

# Output: The integer corresponding to the Xth number in the sorted list

def get_x_from_array(x_position, my_array):

  my_array.sort()
  index_position=x_position-1

  if index_position == 0:
    return 0

  if index_position > len(my_array):
    return 0

  x = my_array[x_position-1]
  return x

my_array = [5, 10, -3 , -3, 7, 9]
x_position= 4
print(get_x_from_array(x_position, my_array))
