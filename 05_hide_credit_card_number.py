
def hide_credit_card_number(credit_card_nr):

  credit_card_nr_list = list(credit_card_nr)
  credit_card_nr_list[-1] = 'X'
  credit_card_nr_list[-2] = 'X'
  credit_card_nr_list[-3] = 'X'
  credit_card_nr_list[-4] = 'X'
  credit_card_number_encrypted = ''.join(map(str,credit_card_nr_list))
  return credit_card_number_encrypted


encrypted_number = hide_credit_card_number('12673478234578')
print(encrypted_number)