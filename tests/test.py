
from SinteticPixels import img
import numpy as np

#test for img module
def img_module_initilizer_test():
	#test auto inferetiation img type.

	#inferetiation gray-scale float
	img_test = img.img(np.ones([32,32], dtype = np.float64))

	assert img_test.img_type == "gray-scale", "should be gray-scale"
	assert img_test.channels_type == "float", "should be float"
	#inferetiation gray-scale int
	img_test = img.img(np.ones([32,32], dtype = np.int32)*100)

	assert img_test.img_type == "gray-scale", "should be gray-scale"
	assert img_test.channels_type == "int", "should be int"
	#inferetiation binary bool
	img_test = img.img(np.ones([32,32], dtype = np.bool))

	assert img_test.img_type == "binary", "should be binary"
	assert img_test.channels_type == "bool", "should be bool"
	#inferetiation gray-scale-alpha float
	img_test = img.img(np.ones([32,32,2], dtype = np.float64))

	assert img_test.img_type == "gray-scale-alpha", "should be gray-scale-alpha"
	assert img_test.channels_type == "float", "should be float"

	#inferetiation gray-scale-alpha int
	img_test = img.img(np.ones([32,32,2], dtype = np.int32)*100)

	assert img_test.img_type == "gray-scale-alpha", "should be gray-scale-alpha"
	assert img_test.channels_type == "int", "should be int"

	#inferetiation rgb float
	img_test = img.img(np.ones([32,32,3], dtype = np.float64))

	assert img_test.img_type == "rgb", "should be rgb"
	assert img_test.channels_type == "float", "should be float"

	#inferetiation rgb int
	img_test = img.img(np.ones([32,32,3], dtype = np.int32)*100)

	assert img_test.img_type == "rgb", "should be rgb"
	assert img_test.channels_type == "int", "should be int"

	#inferetiation rgba float
	img_test = img.img(np.ones([32,32,4], dtype = np.float64))

	assert img_test.img_type == "rgba", "should be rgba"
	assert img_test.channels_type == "float", "should be float"

	#inferetiation rgba int
	img_test = img.img(np.ones([32,32,4], dtype = np.int32)*100)

	assert img_test.img_type == "rgba", "should be rgb"
	assert img_test.channels_type == "int", "should be int"
	
	#TODO: make Indexed deferetiation test.

#execute test for img module
def img_module_testing():
	#initialation.
	img_module_initilizer_test()


#test all parts of the program
def test_all():
	img_module_testing()