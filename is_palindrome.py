from palindrome import is_palindrom

def test_for_palindrome_return_true():
	assert is_palindrome('dad') == True
	assert is_palindrome('12121') == True