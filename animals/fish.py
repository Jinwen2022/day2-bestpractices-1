class Fish:
	def __init__(self):
		self.members = ['Shark','Whale','Zebra Fish']
	def printMembers(self):
		print('Printing members in Fish')
		for member in self.members:
			print('\t%s' % member)