
from SinteticPixels import img
import numpy as np
import pdb
import unittest

#test for img module
def img_module_initilizer_test():
	#test auto inferetiation img type.
	print("=====IMG INITALITATION INFERATION TESTS=====")
	#inferetiation gray-scale float
	img_test = img.img(np.ones([32,32], dtype = np.float64))

	assert img_test.img_type == "gray-scale", "should be gray-scale"
	assert img_test.channels_type == "float", "should be float"
	print("gray-scale float: SUCCESS")
	#inferetiation gray-scale int
	img_test = img.img(np.ones([32,32], dtype = np.int32)*100)

	assert img_test.img_type == "gray-scale", "should be gray-scale"
	assert img_test.channels_type == "int", "should be int"
	print("gray-scale int: SUCCESS")
	#inferetiation binary bool
	img_test = img.img(np.ones([32,32], dtype = np.bool))

	assert img_test.img_type == "binary", "should be binary"
	assert img_test.channels_type == "bool", "should be bool"
	print("binary bool: SUCCESS")
	#inferetiation gray-scale-alpha float
	img_test = img.img(np.ones([32,32,2], dtype = np.float64))

	assert img_test.img_type == "gray-scale-alpha", "should be gray-scale-alpha"
	assert img_test.channels_type == "float", "should be float"
	print("gray-scale-alpha float: SUCCESS")

	#inferetiation gray-scale-alpha int
	img_test = img.img(np.ones([32,32,2], dtype = np.int32)*100)

	assert img_test.img_type == "gray-scale-alpha", "should be gray-scale-alpha"
	assert img_test.channels_type == "int", "should be int"
	print("gray-scale-alpha int: SUCCESS")

	#inferetiation rgb float
	img_test = img.img(np.ones([32,32,3], dtype = np.float64))

	assert img_test.img_type == "rgb", "should be rgb"
	assert img_test.channels_type == "float", "should be float"
	print("rgb float: SUCCESS")

	#inferetiation rgb int
	img_test = img.img(np.ones([32,32,3], dtype = np.int32)*100)

	assert img_test.img_type == "rgb", "should be rgb"
	assert img_test.channels_type == "int", "should be int"
	print("rgb int: SUCCESS")

	#inferetiation rgba float
	img_test = img.img(np.ones([32,32,4], dtype = np.float64))

	assert img_test.img_type == "rgba", "should be rgba"
	assert img_test.channels_type == "float", "should be float"
	print("rgba float: SUCCESS")

	#inferetiation rgba int
	img_test = img.img(np.ones([32,32,4], dtype = np.int32)*100)

	assert img_test.img_type == "rgba", "should be rgb"
	assert img_test.channels_type == "int", "should be int"
	print("rgba int: SUCCESS")

	#inferetiation indexed int
	colors_dictionary = {1 : (0,0,0), 2: (255,255,255), 3 : (100,100,100)}

	img_test = img.img(np.ones([32,32], dtype = np.int32), indexed_colors = colors_dictionary)

	assert img_test.img_type == "indexed", "should be indexed"
	assert img_test.channels_type == "int", "should be int"
	print("indexed int: SUCCESS")
	#TODO: make Indexed INFERATION test.

def img_misselaneus_fuctions_test():
	print('=====IMG MISSLANEUS FUCTIONS=====')

	print('---get_top_scale fuction tests')
	int_case = img.img.get_top_scale('int')
	assert int_case == 255, "should be 255"
	print('int case: SUCCESS')

	float_case = img.img.get_top_scale('float')
	assert float_case == 1, "should be 1"
	print('float case: SUCCESS')

	int_case_np = img.img.get_top_scale(np.int32)
	assert int_case_np == 255, "should be 255"
	print('int case np: SUCCESS')

	float_case_np = img.img.get_top_scale(np.float64)
	assert float_case_np == 1, "should be 1"
	print('float case np: SUCCESS')

	no_exist_case = img.img.get_top_scale('None')
	assert no_exist_case == 0, "should be 0"
	print('no exist case: SUCCESS')

	print('---get_np_type fuction tests')

	int_case = img.img.get_np_type('int')
	assert int_case == np.int32, 'should be np.int32'
	print('int case: SUCCESS')

	float_case = img.img.get_np_type('float')
	assert float_case == np.float64, 'should be np.float64'
	print('float case: SUCCESS')

	bool_case = img.img.get_np_type('bool')
	assert bool_case == np.bool, 'should be np.bool'
	print('bool case: SUCCESS')

	no_exist_case = img.img.get_np_type('None')
	assert no_exist_case is None, 'should be None'
	print('no exist case: SUCCESS')

def img_tester(img, shape_size, channels, nd_type, case_name):
	if  len(img.shape) > shape_size:
		assert img.shape[2] == channels, 'should be {} the channels'.format(channels)
	else:
		assert True, 'not had more than 1 channel'
	assert img.dtype == nd_type, 'should be {} ndarray.dtype'.format(nd_type)

	print("{} case: SUCCESS".format(case_name))

##How i can do a fuction to test a img fuction.
def img_tester(img, func_to_test, channels, nd_dtype, *arg):
	new_img = func_to_test(img, arg)

class test_image_methods(unittest.TestCase):
	
	def setUp(self):
       pass

    def tearDown(self):
       pass

	def test_gray_alpha_to_gray(self):
		pass
	
	def test_gray_alpha_to_rgb(self):
		pass

	def test_gray_alpha_to_rgba(self):
		pass

	def test_gray_alpha_to_binary(self):
		pass

	def test_gray_alpha_to_indexed(self):
		pass

def	img_tester_1_channel(img, nd_type, case_name):
	assert img.dtype == nd_type, 'should be {} ndarray.dtype'.format(nd_type)
	print("{} case: SUCCESS".format(case_name))

def np_convertion_functions_test():

	print('======CONVERTION FUCTION TESTS========')
	print('---from gray-scale convertions')
	#gray np images for testing.

	gray_img_float = np.random.rand(100,100)
	gray_img_int = (gray_img_float*255).astype(int)

	#gray-to-gray-alpha int
	new_img = img.img.gray_to_gray_alpha(gray_img_int)

	if  len(new_img.shape) > 2:
		assert new_img.shape[2] == 2, 'should be 2 the channels'
	else:
		assert True, 'not had more than 1 channel'
	assert new_img.dtype == np.int32, 'should be int32 ndarray.dtype'
	print('gray-scale to gray-scale-alpha int: SUCCESS')

	#gray-to-gray-alpha float
	new_img = img.img.gray_to_gray_alpha(gray_img_float)

	if  len(new_img.shape) > 2:
		assert new_img.shape[2] == 2, 'should be 2 the channels'
	else:
		assert True, 'not had more than 1 channel'
	assert new_img.dtype == np.float64, 'should be float64 ndarray.dtype'
	print('gray-scale to gray-scale-alpha float: SUCCESS')

	#gray_to_rgb int
	new_img = img.img.gray_to_rgb(gray_img_int)

	if  len(new_img.shape) > 2:
		assert new_img.shape[2] == 3, 'should be 3 the channels'
	else:
		assert True, 'not had more than 1 channel'
	assert new_img.dtype == np.int32, 'should be int32 ndarray.dtype'

	#gray_to_rgb float
	new_img = img.img.gray_to_rgb(gray_img_float)

	if  len(new_img.shape) > 2:
		assert new_img.shape[2] == 3, 'should be 3 the channels'
	else:
		assert True, 'not had more than 1 channel'
	assert new_img.dtype == np.float64, 'should be float64 ndarray.dtype'

	#gray_to_rgba int
	new_img = img.img.gray_to_rgba(gray_img_int)
	img_tester(new_img, 2, 4, np.int32, "gray_to_rgba int")
	#gray_to_rgba float
	new_img = img.img.gray_to_rgba(gray_img_float)
	img_tester(new_img, 2, 4, np.float64, "gray_to_rgba float")

	#gray_to_brg int
	new_img = img.img.gray_to_bgr(gray_img_int)
	img_tester(new_img, 2, 3, np.int32, 'gray_to_brg int')
	#gray_to_brg float
	new_img = img.img.gray_to_bgr(gray_img_float)
	img_tester(new_img, 2, 3, np.float64, 'gray_to_brg float')

	#gray_to_binary int
	new_img = img.img.gray_to_binary(gray_img_int, 0.5)
	img_tester_1_channel(new_img, np.bool, 'gray_to_binary int')

	#gray_to_binary float
	new_img = img.img.gray_to_binary(gray_img_int, 0.5)
	img_tester_1_channel(new_img, np.bool, 'gray_to_binary float')

	#gray_to_indexed int
	new_img = img.img.gray_to_indexed(gray_img_int, [0.2, 0.3, 0.6])
	img_tester_1_channel(new_img, np.int32, 'gray_to_indexed int')

	#gray_to_indexed float
	new_img = img.img.gray_to_indexed(gray_img_int, [0.2, 0.3, 0.6])
	img_tester_1_channel(new_img, np.int32, 'gray_to_indexed float')

	print('---from gray-scale convertions')




#execute test for img module
def img_module_testing():
	#initialation.
	img_module_initilizer_test()
	img_misselaneus_fuctions_test()
	np_convertion_functions_test()


#test all parts of the program
def test_all():
	img_module_testing()