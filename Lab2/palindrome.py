def isPalindrome(word):
	if word == word[::-1]:
		return True
if __name__ == "__main__":
	word = raw_input("Gimme a word. Now.")
	print isPalindrome(word)		
	
