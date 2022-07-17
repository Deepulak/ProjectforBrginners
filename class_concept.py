class car:
	carCount = 0
	def __init__(self, color, model):
		self.color = color
		self.model = model
		car.carCount += 1

	def displayCarCount(self):
		print("Total count of cars are %d" % car.carCount)

	def showColorBrand(self):
		print("The color and Brand of the car is ", self.color, self.model)

		# carCount = Class Varable (This value shared across all functions)
		# init = first method which calls class constructor.
		# color model are the instance variable. showColor, showBrand are the python functions

# OOP Concepts
# Object - A unique instance of a data structure 
# that's defined by its class.
# An object comprises both data members
# (class variables and instance variables) and methods

# Instance - An individual object of a certain class.

# Method - A special kind of function that is defined in a class definition

# The first argument of every class method, including init, 
# is always a reference to the current instance of the class.

# By convention, this argument is always named self

# To create a instance object
# First Object
car1 = car("Red", "Ferrri")

# second object 
car2 = car("Black", "Lambhorgini")

# To access attributes
car1.showColorBrand()
car2.showColorBrand()
car2.displayCarCount() 


# The color and brand of the car is Red Ferrari
# Total count of cars are 2