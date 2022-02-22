class Birds:
	def __init__(self):
		self.members=['Eagle','Owl']
	def printMembers(self):
		print('Printing members of the Dangerous Birds class')
		for member in self.members:
			print('\t%s ' % member)
