def divisors(n):
	thelist = [x for x in range(1,n) if (n % x) == 0]	
	for x in thelist:
		print x
if __name__ == "__main__":
	n = int(raw_input("Give me a number. Now."))
	divisors(n)

