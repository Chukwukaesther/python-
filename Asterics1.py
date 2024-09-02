number = 0

print ("Pattern A")
for a in range (0,11):
    number = number + 1
    for aa in range (0, number-1):
        print ('*', end = '')
    print()
print ('')

print ("Pattern B")
for b in range (0,11):
    number = number - 1
    for bb in range (0, number+1):
        print ('*', end = '')
    print()
print ('')

print ("Pattern c")
for a in range (0,11):
    number = number + 1
    for aa in range (0, number-1):
        print ('*', end = '')
    print()
print ('')

print ("Pattern d")
for b in range (0,11):
    number = number - 1
    for bb in range (0, number+1):
        print ('*', end = '')
    print()
