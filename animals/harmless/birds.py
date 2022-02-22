class Birds:
	def __init__(self):
		self.members =['Little bird ','Cute bird','Pretty Bird']
	def printMembers(self):
		print('Printing members of harmless Birds class')
		for member in self.members:
			print('\t%s' % member)
