
from SinteticPixels import img
import numpy as np

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


def np_convertion_functions_test():
	pass


#execute test for img module
def img_module_testing():
	#initialation.
	img_module_initilizer_test()
	img_misselaneus_fuctions_test()


#test all parts of the program
def test_all():
	img_module_testing()