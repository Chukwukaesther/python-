def Highest(numbers): 
	highest = numbers[0]
	for index in range(1,len(numbers)):
		if index > highest:
			highest = index
	return highest
