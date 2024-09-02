def minimum(numbers): 
	min = numbers[0]
	for index in range(1,len(numbers)):
		if index < min:
			min = index
	return min
		
print(minimum([2,3,4,5,6,7,1]))