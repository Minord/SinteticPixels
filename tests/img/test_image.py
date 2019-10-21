import unittest

import numpy as np

from SinteticPixels.img.img import Image

class TestImage(unittest.TestCase):

    def test_binary_autoinferetiation(self):

        #without alpha
        rand_array = np.random.rand(32,32)
        binary_array = rand_array > 0.5

        binary_image = Image(binary_array, 'imagen_test')

        self.assertEqual(binary_image.img_type['type_name'], 'binary', "Should be binary the img type")

        #with alpha it shouldn't be work
        with self.assertRaises(Exception):
            rand_array = np.random.rand(32,32,2)
            binary_array = rand_array > 0.5

            binary_image = Image(binary_array, 'imagen_test', has_alpha = True)


    def test_gray_autoinferetiation(self):
        #without alpha
        rand_array = np.random.rand(32,32)
        gray_image = Image(rand_array, 'imagen_test')

        self.assertEqual(gray_image.img_type['type_name'], 'gray_scale', "Should be gray_scale the img type")

        #with alpha
        rand_array = np.random.rand(32,32,2)
        gray_image = Image(rand_array, 'imagen_test', has_alpha = True)

        self.assertEqual(gray_image.img_type['type_name'], 'gray_scale', "Should be gray_scale the img type")

    def test_rgb_autoinferetiation(self):
        #without alpha
        rand_array = np.random.rand(32,32, 3)

        rgb_image = Image(rand_array, 'imagen_test')
        self.assertEqual(rgb_image.img_type['type_name'], 'rgb', "Should be rgb the img type")

        #with alpha
        rand_array = np.random.rand(32,32,4)
        rgb_image = Image(rand_array, 'imagen_test', has_alpha = True)

        self.assertEqual(rgb_image.img_type['type_name'], 'rgb', "Should be rgb the img type")
