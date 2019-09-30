import numpy as np
import pdb



def expand_img(ndarray ,left, right, up, down):
	"""
	this is for expand the borders of the image with the same information
	of the borders.

	Parameters
	---------
		ndarray - numpy ndarray with the base information

		left - int - the num of columns to add in left

		right - int - the num of columns to add in right

		up - int - the num of rows to add in top

		down - int - the number of rows to add in down

	Returns
	-------
		the final expanded result ndarray numpy
	"""
	if left > 0:
		#get the neighbor column for duplicate it
		to_add = ndarray[:, 0]#get the firts column
		to_add = to_add[None] #add new axis 
		to_add = np.repeat(to_add.T, left, axis = 1)
		#add the extrapolation to final result
		ndarray = np.concatenate((to_add ,ndarray), axis = 1)

	if right > 0:
		#get the neighbor column for duplicate it
		to_add = ndarray[:, -1] #get the last column
		to_add = to_add[None] #add new axis
		to_add = np.repeat(to_add.T, right, axis = 1)
		#add the extrapolation to final result
		ndarray = np.concatenate((ndarray, to_add), axis = 1)
	if up > 0:
		#get the neighbor row for duplicate it
		to_add = ndarray[0, :] #get the first row
		to_add = to_add[None] #add new axis
		to_add = np.repeat(to_add, up, axis = 0)
		#add the extrapolation to final result
		ndarray = np.concatenate((to_add, ndarray), axis = 0)
	if down > 0:
		#get the neighbor column for duplicate it
		to_add = ndarray[-1, :] #get the first row
		to_add = to_add[None] #add new axis
		to_add = np.repeat(to_add, down, axis = 0)
		#add the extrapolation to final result
		ndarray = np.concatenate((ndarray, to_add), axis = 0)

	return ndarray
		
#TODO: Check spelling
#TODO: Check and test some extreme cases like 1 by 1 kernel or a rare kernel
#and to check if the logic is correct. but by now is seems like it work
def convolution2D_float(ndarray, kernel, kernel_pivot):
	"""
	make a convolution process with an kernel and we can set 
	any origin to that kernel and make convolutions with odd kernels

	Parameters
	-----------
		ndarray - ndarray numpy - the original image in which we will make the convolution

		kernel - ndarray numpy - the kernel we going to use

		kernel pivot - int tuple - indexes of origin kernel like (x, y) (1, 5) etc with
								   values inside of kernel bounds

	Return
	--------
		new_ndarray - ndarray numpy - the final result with applied convolution process.
	"""
	#validation of arrays types
	assert ndarray.dtype == np.float, 'Invalid dtype of ndarray should be float'
	assert kernel.dtype == np.float, 'Invalid dtype of kernel should be float'
	assert ndarray.ndim == 2, 'Invalid ndarray dimension'
	assert kernel.ndim == 2, 'Invalid kernel dimension'
	#check if the kernel_pivot is valid
	height_kernel, width_kernel = kernel.shape
	x_pivot, y_pivot = kernel_pivot

	if not (x_pivot >= 0 and x_pivot < width_kernel) and (y_pivot >= 0 and y_pivot < height_kernel):

		assert False, 'Invalid pivot coordinates'

	flatten_kernel = kernel.flatten()

	#create new ndarray object for store the result
	result_ndarray = np.zeros(ndarray.shape, dtype = float)

	#get the actual shape for 
	height, width = ndarray.shape
	
	#calculate kernel bounds
	x_min, x_max = (x_pivot), ((width_kernel-1) - x_pivot)
	y_min, y_max = (y_pivot), ((height_kernel-1) - y_pivot)

	#change the bounds of my array with concatenate fuctions

	left, right, up, down = x_min, x_max, y_min, y_max
	ndarray = expand_img(ndarray, left, right, up, down)

	x_init, x_end = x_min, x_min + width
	y_init, y_end = y_min, y_min + height
	#loops for access to ndarrays
	for x in range(x_init, x_end ):
		for y in range(y_init, y_end ):
			#get the data of original image
			ponderate_values = ndarray[(y - y_min):(y + y_max + 1) , # y range to indexed
									   (x - x_min):(x + x_max) + 1]  # x range to indexed
			ponderate_values = ponderate_values.flatten()

			#get the dot product for the ponderate sum
			result_ndarray[x - x_init, y - y_init] = np.dot(ponderate_values, flatten_kernel) 

	return result_ndarray


#TODO: implements this methods
def stamp2D_float(self, ndarray, brush):
		pass




#this is for the operations for float ndarrays
class FloatOperations():
	def __init__(self):
		pass

	#operations with 1 ndarrays
	

	#operations with 2 ndarrays
	
	def sum(self, ndarray1, ndarray2):
		pass
	
	def diference(self, ndarray1, ndarray2):
		pass

	def multiply(self, ndarray1, ndarray2):
		pass

	def division(self, ndarray1, ndarray2):
		pass


#this is for the operations for int ndarrays
class IntOperations():
	def __init__(self):
		pass

	#operations with 1 ndarrays
	def convolution(self, kernel):
		pass

	def stamp(self, brush):
		pass

	#operations with 2 ndarrays
	# ...


#this is for the general operations with boolean ndarray
class BoolOperations():
	def __init__(self):
		pass

	#operations with 1 ndarrays
	def convolution(self, ndarray, kernel):
		pass

	def stamp(self, ndarray, brush):
		pass

	#operations with 2 ndarrays
	def union(self, ndarray1, ndarray2):
		pass

	def interception(self, ndarray1, ndarray2):
		pass

	def diference(self, ndarray1, ndarray2):
		pass