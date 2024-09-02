Def is_palindrome(word):
	reversed_word = ""
	for index in range(len(word)-1, -1, -1) :
		reversed_word += word[index]
	return word == reversed_word