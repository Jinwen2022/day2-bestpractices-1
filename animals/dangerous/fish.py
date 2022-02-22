class Fish:
	def __init__(self):
		self.members = ['Shark','fish that eat your ass','Tiger shark']
	def printMembers(self):
		print('Printing members in dangerous Fish class')
		for member in self.members:
			print('\t%s' % member)
