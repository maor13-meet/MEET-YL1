if __name__ == "__main__":
	people = []
	for x in xrange(3):
		name = raw_input("Whats your name?")
		age = raw_input("Whats your age?")
		dic = {"name":name, "age":age}
		people.append(dic)
	print people
	
