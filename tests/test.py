
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
	pass

#execute test for img module
def img_module_testing():
	#initialation.
	img_module_initilizer_test()


#test all parts of the program
def test_all():
	img_module_testing()