lucky_Number = 5

for count in range(1,4):
	digit = int(input("Enter lucky_Number: "))
	if digit == lucky_Number:
		print("Congratulation you passed")
		break
	else:
			print("Try again later") 