import unittest
import numpy as np
import matplotlib.pyplot as plt
import pdb

from SinteticPixels.img import operations

visualizate_expand_img =  False
visualizate_convolution2D_float = False


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

	def test_convolution2D_float(self):
		width, height = 32, 32
		random_array = np.random.rand(height, width)

		random_kernel = np.random.rand(3,3)
		random_kernel = random_kernel / random_kernel.sum()

		kernel_pivot = (1, 1)

		new_random_array = operations.convolution2D_float(random_array, random_kernel, kernel_pivot)

		if visualizate_convolution2D_float:
			plt.imshow(random_array)
			plt.show()
			plt.imshow(new_random_array)
			plt.show()

		self.assertEqual(random_array.shape, new_random_array.shape)