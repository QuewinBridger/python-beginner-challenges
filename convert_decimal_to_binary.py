
def convert_decimal_to_binary(decimal):

  if decimal >=1:
    convert_decimal_to_binary(decimal//2)
    save_binary_into_array(decimal%2)

binary_array=[]
def save_binary_into_array(binary):
  binary_array.append(binary)

decimal = 17
binary = convert_decimal_to_binary(decimal=decimal)
print(binary_array)