class Integer(object):
	def __init__(self, num, pos):
		self.number = num
		self.positive = pos
	def display(self):
		print self.positive + str(self.number)
	def intNumber(self):
		if self.positive == "-":
			return self.number*-1
		else:
			return self.number
class NegativeInteger(Integer):
	def __init__(self, num):
		super(NegativeInteger, self).__init__(num, "-")
	def display(self):
		Integer.display(self)
		print " Instance of Negative "
	#	print self.positive + str(self.number) + " Damn!"
	def intNumber(self):
		return self.number*-1

if __name__=="__main__":
	n = Integer(3,"-")
	n2 = NegativeInteger(4)
	n2.display()

		
		
	
	
	 	
