class VendingMachine:

	def __init__(self,inMachine):
		self.venMilk = inMachine.venMilk

		try:
			if hasattr(inMachine,"venSugar"):
				self.venSugar = inMachine.venSugar
		except:
			pass

		try:
			if hasattr(inMachine,"venCoffeepowder"):
				self.venCoffeepowder = inMachine.venCoffeepowder
		except:
			pass

		try:
			if hasattr(inMachine,"venTeapowder"):
				self.venTeapowder = inMachine.venTeapowder
		except:
			pass

		try:
			if hasattr(inMachine, "venWater"):
				self.venWater = inMachine.venWater
		except:
			pass

	def __str__(self):
		return f'{self.__dict__}'

	class innerMachine:

		def __init__(self,milk):
			self.venMilk = milk

		def set_sugar(self,sugar):
			self.venSugar = sugar
			return self

		def set_coffee(self,coffee):
			self.venCoffeepowder = coffee
			return self

		def set_tea(self,tea):
			self.venTeapowder = tea
			return self

		def set_water(self,water):
			self.venWater = water
			return self

		def build(self):
			return VendingMachine(self)

		def __str__(self):
			return f'{self.venMilk}'


obj = VendingMachine.innerMachine(milk="250ml").set_coffee("Bru").set_sugar('20gm').set_tea('society').set_water('50ml').build()
print(type(obj))
print(obj)