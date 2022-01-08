#!/usr/bin/python3
from math import sqrt, acos, pi
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

	def magnitude(self):
		mag_value = 0
		n = len(self.coordinates)
		for i in range(n):
			mag_value += self.coordinates[i]**2
		return 'Magnitude of {} is {:.3f}'.format(self.coordinates, sqrt(mag_value))

	def normalization(self):
		try:
			value = 0
			n = len(self.coordinates)
			for i in range(n):
				value += self.coordinates[i]**2
			mag_value = sqrt(value)
			vector_scalar = 1 / mag_value
			return (self.coordinates,self.times_scalar(vector_scalar))
		except ZeroDivisionError:
			raise Exception('Cannot normalize the zero vector')

	def dot_product(self, v):
		return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
		

	def angle_between_vectors(self, v, in_degrees=False):
		try:
			v1 = self.normalization()
			v2 = v.normalization()
			angle_in_radians = acos(v1.dot_product(v2))

			if in_degrees:
				degrees_per_radian = 180. / pi
				return (angle_in_radians * degrees_per_radian)
			else:
				return angle_in_radians

		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception('Cannot compute an angle with the zero vector')
			else:
				raise e

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

#magnitude of a vector
my_vector4 = Vector([-0.221, 7.437])
print (Vector.magnitude(my_vector4))
my_vector5 = Vector([8.813, -1.331, -6.247])
print(Vector.magnitude(my_vector5))

#normalization of a vector
my_vector6 = Vector([5.581, -2.136])
print (Vector.normalization(my_vector6))
my_vector7 = Vector([1.996, 3.108, -4.554])
print(Vector.normalization(my_vector7))

#Dot product of two vectors
print (Vector.dot_product(my_vector1, my_vector2))

#angle between two vectors
print (Vector.angle_between_vectors(my_vector1, my_vector2, True))