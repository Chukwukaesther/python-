import random

LUCKY_NUMBER = random.randrange(1,10)

while  LUCKY_NUMBER != userinput:
		userinput = int(input("Enter Lucky number: "))
		if LUCKY_NUMBER == userinput:
		
			print("Congratulations you passed") 
		        break
		else:
			print("Try again later") 