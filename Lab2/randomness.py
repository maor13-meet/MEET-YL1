from random import randint

def random():
	prob = int(raw_input("What probability is heads (%)? "))
	randomNumber = randint(0,100)
	if randomNumber < prob:
		print "Heads"
	else:
		print "Tails"
def flipItAlot():
	times = int(raw_input("Flip it how many times? "))
	coins = []	
	for t in range(times):
		randomNumber = randint(0,1)
		if randomNumber == 0:
			coins.append("heads")
		else:
			coins.append("tails")
	return coins

print flipItAlot()
