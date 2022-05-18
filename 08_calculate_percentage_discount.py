from dis import dis


def calculate_percentage_discount(original_price, discounted_price):
  percentage_discount = (1-discounted_price/original_price)*100
  return round(percentage_discount)

original_price = float(input("enter original price of item "))
discounted_price = float(input("enter the discounted price of the item "))

print(calculate_percentage_discount(original_price, discounted_price))