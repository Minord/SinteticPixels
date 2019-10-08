import unittest
import numpy as np
import matplotlib.pyplot as plt
import pdb

from SinteticPixels.img import operations

visualizate_expand_img =  False
visualizate_convolution2D_float = False
visualizate_stamp2D = False


class TestOperations(unittest.TestCase):
	
	def test_expand_img(self):

		width, height = 32, 32
		random_array = np.random.rand(height, width)

		left, right, up, down = 10, 5, 8, 2

		#there we haver bigger problems
		new_random_array = operations.expand_img(random_array, left, right, up, down)

		new_height ,new_width = new_random_array.shape

		#visualizate 
		if visualizate_expand_img:
			plt.imshow(random_array)
			plt.show()
			plt.imshow(new_random_array)
			plt.show()
			
			

		#check x bounds
		self.assertEqual(new_width, left + right + width)
		#check y bounds
		self.assertEqual(new_height, up + down + height)

	def test_convolution2D(self):
		width, height = 32, 32
		random_array = np.random.rand(height, width)

		random_kernel = np.random.rand(3,3)
		random_kernel = random_kernel / random_kernel.sum()

		kernel_pivot = (1, 1)

		new_random_array = operations.convolution2D(random_array, random_kernel, kernel_pivot)

		if visualizate_convolution2D_float:
			plt.imshow(random_array)
			plt.show()
			plt.imshow(new_random_array)
			plt.show()

		self.assertEqual(random_array.shape, new_random_array.shape)

	def test_point_into_bound(self):

		#Test -x case
		shape = (64, 32) #in order (y,x) by numpy 
		point = (-3, 10) # in (x, y)

		with self.assertRaises(Exception):
			operations.point_into_bound(shape, point, 'test_array')

		#Test +x case
		shape = (64, 32) #in order (y,x) by numpy 
		point = (100, 10) # in (x, y)

		with self.assertRaises(Exception):
			operations.point_into_bound(shape, point, 'test_array')


		#Test -y case
		shape = (64, 32) #in order (y,x) by numpy 
		point = (10, -10) # in (x, y)

		with self.assertRaises(Exception):
			operations.point_into_bound(shape, point, 'test_array')

		#Test +y case
		shape = (64, 32) #in order (y,x) by numpy 
		point = (10, 1000) # in (x, y)

		with self.assertRaises(Exception):
			operations.point_into_bound(shape, point, 'test_array')


	def test_retrict_range_index(self):

		range_t = (0, 10)

		for x in range(-5 , 15):
			#if the range is in normal valid range
			if x >= range_t[0] and x < range_t[1]: 
				operations.retrict_range_index(x, range_t)
			#if the range is in negative out of range
			elif x < range_t[0]:
				result = operations.retrict_range_index(x, range_t)
				self.assertEqual(result, range_t[0])
			#if the range is in positive out of range
			elif x >= range_t[1]:
				result = operations.retrict_range_index(x, range_t)
				self.assertEqual(result, range_t[1])


	def test_valid_dtype_assertion(self):
		
		actual_dtype = np.float
		expected_dtypes = (np.float, np.int)

		#should be succes
		operations.valid_dtype_assertion(expected_dtypes, actual_dtype, 'test_type')
		actual_dtype = np.bool
		#should be fail
		with self.assertRaises(Exception):
			operations.valid_dtype_assertion(expected_dtypes, actual_dtype, 'test_type')

		#should be succes
		actual_dtype = int
		operations.valid_dtype_assertion(expected_dtypes, actual_dtype, 'test_type')

	def test_valid_ndim_assertion(self):
		actual_dimention = 2
		expected_dimentions = (2,)
		#should be succes
		operations.valid_ndim_assertion(expected_dimentions, actual_dimention, 'test_dimention')

		actual_dimention = 3
		#should be fail
		with self.assertRaises(Exception):
			operations.valid_ndim_assertion(expected_dimentions, actual_dimention, 'test_dimention')

	def test_validate_ndarray(self):

		expected_dtypes = (np.float, np.int)
		expected_dimentions = (2,)

		ndarray = np.ones((32,32), np.float)
		operations.validate_ndarray(ndarray, expected_dtypes, expected_dimentions, 'test_ndarray')

		ndarray = np.ones((32,32), np.int)
		operations.validate_ndarray(ndarray, expected_dtypes, expected_dimentions, 'test_ndarray')

		ndarray = np.ones((32,32), np.bool)
		with self.assertRaises(Exception):
			operations.validate_ndarray(ndarray, expected_dtypes, expected_dimentions, 'test_ndarray')

		ndarray = np.ones((32,32,3), np.int)
		with self.assertRaises(Exception):
			operations.validate_ndarray(ndarray, expected_dtypes, expected_dimentions, 'test_ndarray')

	def test_validate_common(self):
		#should be succes
		ndarray = np.ones((32,32), np.float)
		operations.validate_common(ndarray, 'test_ndarray')

		ndarray = np.ones((32,32), np.float)
		operations.validate_common(ndarray, 'test_ndarray')

		#should be fail
		ndarray = np.ones((32,32), np.bool)
		with self.assertRaises(Exception):
			operations.validate_common(ndarray, 'test_ndarray')

		ndarray = np.ones((32,32, 3), np.int)
		with self.assertRaises(Exception):
			operations.validate_common(ndarray, 'test_ndarray')

	def test_stamp2D(self):

		stamp = np.array([[1,1,0],[1,0.5,1],[0,1,1]])
		stamp_pivot = (0, 0)

		test_img = np.random.rand(32, 32) / 10

		stamp_pivot = (0, 0)
		stamp_point = (3,3)
		test_img_stamping = operations.stamp2D(test_img, stamp, stamp_pivot, stamp_point)

		stamp_pivot = (1, 1)
		stamp_point = (7,0)
		test_img_stamping = operations.stamp2D(test_img_stamping, stamp, stamp_pivot, stamp_point)

		stamp_pivot = (2, 2)
		stamp_point = (11,31)
		test_img_stamping = operations.stamp2D(test_img_stamping, stamp, stamp_pivot, stamp_point)

		if visualizate_stamp2D:
			plt.imshow(test_img)
			plt.show()
			plt.imshow(test_img_stamping)
			plt.show()