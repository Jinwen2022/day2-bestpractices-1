class Fish:
	def __init__(self):
		self.members =['Shark','Fish that eat your ass']
	def printMembers(self):
		print('Printing members of harmless Fish class')
		for member in self.members:
			print('\t%s' % member)
