class Birds:
	def __init__(self):
		self.members =['Sparrow','Robin','Swan']
	def printMembers(self):
		print('Printing members of Birds class')
		for member in self.members:
			print('\t%s' % member)
