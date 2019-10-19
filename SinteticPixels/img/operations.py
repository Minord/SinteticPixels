import numpy as np
import pdb



#TODO: maybe i should make what this can handle with others expand values adding , expand_value = None
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
#TODO: make a bechmark
#TODO: this method only accept float ndarray i whant accept int too
def convolution2D(ndarray, kernel, kernel_pivot):
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

def point_into_bound(bounds, point, array_name):
	"""
	Check if the point values are not outside of bounds value and raise the assets

	Parameters
	----------
	bounds - int tuple - the shape of a array with the format of (heigth, width)

	point - int tuple - the point to check

	array_name - string - the name for make more despriptive the assets

	"""
	height, width = bounds #get ndarray shape
	x, y = point #get the components of stamp_point
	#validate in x
	assert (x >= 0 and x < width), "out of {} bounds in x axis in stamp_point".format(array_name)
	#validate in y
	assert (y >= 0 and y < height), "out of {} bounds in y axis in stamp_point".format(array_name)

def retrict_range_index(value, range):
	"""
	it cut off in the border of range if the value are outside of range

	Parameters
	-----------
	value - int - is the value that we going to limit if it is out of range

	range - int - es el rango que limita el valor con el formato (min, max)
	donde max no está en el rango por razones de índice  #FIXME: tanslate this to english
	"""
	min, max = range
	if value < min:
		return min
	elif value >= max:
		return max
	return value

def valid_dtype_assertion(expected_dtypes, actual_dtype, name):
	"""
	Check if the actual dtype is in expected_dtypes tuple

	Parameters
	-----------
	expected_dtypes - dtypes tuple - this are the set of valid types.
	actual_dtype - dtype - the actual dtype for check
	name - string - the name for the assertion error message
	"""
	assert (actual_dtype in expected_dtypes), "Invalid dtype of {} should be {}".format(name, str(expected_dtypes))
	
def valid_ndim_assertion(expected_dimentions, actual_dimention, name):
	"""
	Check if the actual ndim is in expected ndim tuple

	Parameters
	----------
		expected_dimentions - int tuple - this are the set of valid ndim.
		actual_dimention - int - the actual ndim for check
		name - string - the name for the assertion error message
	"""
	assert (actual_dimention in expected_dimentions), "Invalid ndim of {} should be {}".format(name, str(expected_dimentions))

def validate_ndarray(ndarray, expected_dtypes, expected_dimentions, name):
	"""
	this is for check a ndarray has valid of dtype and ndim.

	Parematers
	----------
	ndarray - ndarray numpy - the ndarray form which the properties will be obtained
	expected_dtypes - dtypes tuple - this are the set of valid types.
	expected_dimentions - int tuple - this are the set of valid ndim.
	name - string - the name for the assertion error message
	"""
	valid_dtype_assertion(expected_dtypes, ndarray.dtype, name)
	valid_ndim_assertion(expected_dimentions, ndarray.ndim, name)

def validate_common(ndarray, name):
	"""
	check if ndarray has 2 dimensions only and if it has float or int dtypes

	Parameters
	----------- 
	ndarray - ndarray numpy - the ndarray form which the properties will be obtained
	name - string - the name for the assertion error message
	"""
	validate_ndarray(ndarray,(np.float, np.int), (2,) , name)

def stamp2D(ndarray, brush, brush_pivot, stamp_point, neutral_value = 0):
	"""
	Stamp pixels according to a brush, you can choose the brush pivot
	and stamp point

	Parameters
	-----------
	ndarray - ndarray numpy - original image to stamp
	brush - ndarray numpy - brush to stamp
	brush_pivot - int tuple - brush origin it has to be between brush bounds in (x, y) format
	stamp_point - int tuple - stamp point it has to be between ndarray img bounds in (x, y) format
	neutral_value - num - a value in brush what is go to be ignore in the stamp
	"""
	#check if ndarray inputs has valid propierties
	validate_common(ndarray, 'ndarray')
	validate_common(brush, 'brush')

	#check if we have a valid stamp point
	point_into_bound(ndarray.shape, stamp_point, 'ndarray')

	#check if the brush pivot point is valid
	point_into_bound(brush.shape, brush_pivot, 'brush')

	#get the components of the shapes of ndarray and brush
	height, width = ndarray.shape
	brush_height, brush_width = brush.shape

	#get the components of stamp and brush points
	x_stamp, y_stamp = stamp_point
	x_pivot, y_pivot = brush_pivot

	#get the bounds for iterate over them
	x_min, x_max = (x_stamp - x_pivot), (x_stamp + brush_width - x_pivot)
	y_min, y_max = (y_stamp - y_pivot), (y_stamp + brush_height - y_pivot)

	#validate the loop indexes
	x_min = retrict_range_index(x_min, (0, width))
	x_max = retrict_range_index(x_max, (0, width))
	y_min = retrict_range_index(y_min, (0, height))
	y_max = retrict_range_index(y_max, (0, height))

	#create a copy of the original ndarray
	new_ndarray = np.array(ndarray)

	for x in range(x_min, x_max):
		for y in range(y_min, y_max):
			#get the index in brush arrray
			x_brush = x - x_stamp + x_pivot
			y_brush = y - y_stamp + y_pivot

			#check if the value is null
			if brush[y_brush, x_brush] != neutral_value:
				new_ndarray[y, x] = brush[y_brush, x_brush]
	return new_ndarray


def replace():
	pass

def operation_coordinates():
	pass

def fusion():
	pass