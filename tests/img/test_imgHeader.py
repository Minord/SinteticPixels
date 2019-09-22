import unittest
from SinteticPixels.img import imgHeader as ih
from SinteticPixels.img.imgHeader import ImgHeader 


img_type_test = {
	'name': 'test_type',
	'scales': (0, 1, float),
	'channels': 1,
	'alpha': False,
	'operation_type': 'universal_operations',
	'to_conv': None,
	'from_conv': None
}

img_type_test2 = {
	'name': 'test_type2',
	'scales': (0, 1, float),
	'channels': 1,
	'alpha': False,
	'operation_type': 'universal_operations',
	'to_conv': None,
	'from_conv': None
}

class TestImgHeader(unittest.TestCase):
	
	def test_imgHeader_construntor(self):
		

	def test_completeName(self):
		imgHeader_test = ImgHeader(img_type_test, 'img1', alpha = False)
		correct_complete_name = 'img1_test_type'

		self.assertEqual(imgHeader_test.completeName(), correct_complete_name)

		imgHeader_test = ImgHeader(img_type_test2, 'img2', alpha = True)
		correct_complete_name = 'img2_test_type2'

		self.assertEqual(imgHeader_test.completeName(), correct_complete_name)

	def test_