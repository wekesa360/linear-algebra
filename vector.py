#!/usr/bin/python3
class Vector():
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


	def plus(self, v):
		new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def minus(self, v):
		new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def times_scalar(self, c):
		new_coordinates = [c*x for x in self.coordinates]
		return Vector(new_coordinates)
	

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)


	def __eq__(self, v):
		return self.coordinates == v.coordinates



#creating vectors
my_vector = Vector([2,3,4])
print (my_vector)

#comparing vectors
my_vector1 = Vector([1,2,3])
my_vector2 = Vector([1,2,3])
print (my_vector1 == my_vector2)


my_vector1 = Vector([1,3,3])
my_vector2 = Vector([-1,1,3])
print (my_vector1 == my_vector2)

#addition of vectors 
print (Vector.plus(my_vector1,my_vector2))

#subtraction of vectors 
print (Vector.minus(my_vector1,my_vector2))

#times scaler of vectors 
print (Vector.times_scalar(my_vector1, 2))
