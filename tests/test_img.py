from SinteticPixels.img import img

import numpy as np
import unittest

class img_conv_test(unittest.TestCase):
	
	def test_invalid_channel_num_case(self):
		invalid_img = np.full((64,64,2), 255, dtype=np.float64)
		with self.assertRaises(Exception):
			test_img = img.conv_img(invalid_img)
	
	def test_invalid_type_case(self):
		invalid_img = np.full((64,64,3), 255, dtype=np.int32)
		with self.assertRaises(Exception):
			test_img = img.conv_img(invalid_img)

	def test_noalpha_noalpha(self):
		no_alpha_img = np.full((64,64,3), 255, dtype=np.float64)
		convertion_format_img = img.conv_img(no_alpha_img)
		new_img = convertion_format_img.get_data()
		self.assertEqual(3, new_img.shape[2])

	def test_noalpha_alpha(self):
		no_alpha_img = np.full((64,64,3), 255, dtype=np.float64)
		convertion_format_img = img.conv_img(no_alpha_img)
		new_img = convertion_format_img.get_data(alpha=True)
		self.assertEqual(4, new_img.shape[2])

	def test_alpha_noalpha(self):
		no_alpha_img = np.full((64,64,4), 255, dtype=np.float64)
		convertion_format_img = img.conv_img(no_alpha_img)
		new_img = convertion_format_img.get_data()
		self.assertEqual(3, new_img.shape[2])

	def test_alpha_alpha(self):
		no_alpha_img = np.full((64,64,4), 255, dtype=np.float64)
		convertion_format_img = img.conv_img(no_alpha_img)
		new_img = convertion_format_img.get_data(alpha=True)
		self.assertEqual(4, new_img.shape[2])

class test_img_convertion(unittest.TestCase):
	

	def conv_img_test(self, conv):
		self.assertEqual(3, conv.get_data().shape[2])
		self.assertEqual(4, conv.get_data(alpha=True).shape[2])
		self.assertEqual(np.float64, conv.get_data().dtype)

	def np_image_test(self, np_image, channels, np_type):
		actual_channels = np_image.shape[-1]
		if len(np_image.shape) <= 2:
			actual_channels = 1
		self.assertEqual(channels, actual_channels)
		self.assertEqual(np_type, np_image.dtype)

	def fuction_to_conv_test(self, shape , conv_func):
		img_255 = np.full(shape, 255, np.int32)
		img_1 = np.ones(shape, np.float64)

		img1 = conv_func(img_255, (0,255))
		img2 = conv_func(img_1, (0, 1))
		
		self.conv_img_test(img1)
		self.conv_img_test(img2)

	def fuction_from_conv_test(self, shape , conv_func, from_conv_func, channels):
		img_255 = np.full(shape, 255, np.int32)
		img_1 = np.ones(shape, np.int64)

		conv1 = conv_func(img_255, (0,255))
		conv2 = conv_func(img_1, (0, 1))

		img1 = from_conv_func(conv1, (0, 1), np.float64)
		img2 = from_conv_func(conv2, (0, 255), np.int32)

		self.np_image_test(img1, channels, np.float64)
		self.np_image_test(img2, channels, np.int32)

	#gray_scale test
	def test_gray_scale_to_conv(self):
		function_tested =  img.img.gray_scale_to_conv
		self.fuction_to_conv_test((64,64), function_tested)

	def test_conv_to_gray_scale(self):
		fuction_1 = img.img.gray_scale_to_conv
		fuction_tested =  img.img.conv_to_gray_scale
		self.fuction_from_conv_test((64, 64), fuction_1, fuction_tested, 1)

	def test_gray_scale_alpha_to_conv(self):
		function_tested =  img.img.gray_scale_alpha_to_conv
		self.fuction_to_conv_test((64,64,2), function_tested)

	def test_conv_to_gray_scale_alpha(self):
		fuction_1 = img.img.gray_scale_alpha_to_conv
		fuction_tested =  img.img.conv_to_gray_scale_alpha
		self.fuction_from_conv_test((64, 64,2), fuction_1, fuction_tested, 2)
	
	#rgb test
	def test_rgb_to_conv(self):
		function_tested =  img.img.rgb_to_conv
		self.fuction_to_conv_test((64,64,3), function_tested)

	def test_conv_to_rgb(self):
		fuction_1 = img.img.rgb_to_conv
		fuction_tested =  img.img.conv_to_rgb
		self.fuction_from_conv_test((64, 64,3), fuction_1, fuction_tested, 3)

	#rgba test
	def test_rgba_to_conv(self):
		function_tested =  img.img.rgba_to_conv
		self.fuction_to_conv_test((64,64,4), function_tested)

	def test_conv_to_rgba(self):
		fuction_1 = img.img.rgba_to_conv
		fuction_tested =  img.img.conv_to_rgba
		self.fuction_from_conv_test((64, 64, 4), fuction_1, fuction_tested, 4)

	#bgr test
	def test_bgr_to_conv(self):
		function_tested =  img.img.bgr_to_conv
		self.fuction_to_conv_test((64,64,3), function_tested)

	def test_conv_to_bgr(self):
		fuction_1 = img.img.bgr_to_conv
		fuction_tested =  img.img.conv_to_bgr
		self.fuction_from_conv_test((64, 64, 3), fuction_1, fuction_tested, 3)

	#binary test
	def test_binary_to_conv(self):
		img_bool = np.ones((32, 32), np.bool)

		img1 = img.img.binary_to_conv(img_bool)
		
		self.conv_img_test(img1)
	
	def test_conv_to_binary(self):
		img_bool = np.ones((32, 32), np.bool)

		conv = img.img.binary_to_conv(img_bool)
		
		img_b = img.img.conv_to_binary(conv)

		self.assertEqual(img_b.dtype, np.bool)
		self.assertEqual(len(img_b.shape), 2)
		
	#indexed test
	#def test_indexed_to_conv(self):
		#pass
	
	#def test_conv_to_indexed(self):
		#pass


if __name__ == '__main__':
    unittest.main()

