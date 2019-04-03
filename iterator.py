#Range Function


class MyRangeFunction:
	def __init__(self, start=0, stop=None):
		self.start = start
		self.stop = stop

	def __iter__(self):
		self.initial = True
		return self

	def __next__(self):
		if self.start < self.stop-1:
			if self.initial:
				self.initial = False
				return self.start
			else:
				self.start = self.start+1
				return self.start
		raise StopIteration


for item in iter(MyRangeFunction(5, 50)):
	print(item)

"""
print Table using iterator

"""


class Table:
	def __init__(self, num):
		self.startTable = num
		self.stopTable = num*10

	def __iter__(self):
		self.startPoint = self.startTable
		self.initial = True
		return self

	def __next__(self):
		if self.startTable<self.stopTable:
			if self.initial:
				self.initial = False
				return self.startTable
			self.startTable += self.startPoint
			return self.startTable
		raise StopIteration


for item in iter(Table(12)):
	print(item)

