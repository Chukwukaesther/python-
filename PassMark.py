pass_mark = 45
pass_student =0
fail_student = 0
total_passed = 0
total_failed = 0
count =0

for scores in range (15):
	scores = int(input('Enter scores of student:'))
	if scores >= pass_mark:
		total_passed +=1
	if scores < pass_mark:
		total_failed+=1

	count +=1
print("the total_passed student is :", total_passed)
print("the total_failed student is :", total_failed)




  
 
