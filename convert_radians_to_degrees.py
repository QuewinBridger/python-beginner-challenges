import math


def convert_radians_to_degrees(radians):
  degrees = radians*math.pi
  return degrees


degrees = convert_radians_to_degrees(5)
print(degrees)