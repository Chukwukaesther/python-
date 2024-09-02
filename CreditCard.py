def validate_atm_card(card_number):
	card_number = card_number.replace(' ', '')  
	if not card_number.isdigit():
  		return "Invalid input. Please enter only digits" 
	if len(card_number) < 12:	
		return "Invalid"
	if len(card_number) > 19:
		return "Valid"
    
first_digit = int(card_number[0])
if first_digit == 4:
        	card_type = "Visa"
elif first_digit == 5:
        	card_type = "Mastercard"
elif first_digit == 3 and int(card_number[1]) in [7]:
        	card_type = "American Express"
elif first_digit == 6:
		card_type = "Discover card"
else:
        card_type = "Unknown"		
  return type
    
 
digits = [int(x) for x in card_number]
odd_digits = digits[-1::-2]
even_digits = digits[-2::-2]
checksum = sum(odd_digits) + sum(sum(divmod(d * 2, 10)) for d in even_digits)
    
if checksum % 10 == 0:
       		 return f"The {card_type} card is valid"
else:
       		 return f"The {card_type} card is invalid"


card_number = input(len("Enter your ATM card number: "))

print(validate_atm_card(card_number))
print(checksum)