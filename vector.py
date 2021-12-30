#!/usr/bin/python3
class Vector():
	coordinates = (0, 0)
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)
		except ValueError:
			raise ValueError('The coordinates must be nonempty')
		
		except TypeError:
			raise TypeError('The coordiantes must be an iterable')


	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)


	def __eq__(self, v):
		return self.coordinates == v.coordinates

#creating coordinates 
my_vector = Vector([2,3,4])
print (my_vector)

#comparing cooordinates
my_vector1 = Vector([1,2,3])
my_vector2 = Vector([1,2,3])
print (my_vector1 == my_vector2)


my_vector1 = Vector([1,3,3])
my_vector2 = Vector([-1,1,3])
print (my_vector1 == my_vector2)
