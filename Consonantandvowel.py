count_consonant = 0
count_vowel = 0
vowel = ['a','e','i','o','u']

user_Input = input("Enter words: ")
for i in user_Input:
	if i in vowel:
		count_vowel += 1
	else:
		count_consonant +=1
print(f"vowel {count_vowel}  consonant {count_consonant}")


