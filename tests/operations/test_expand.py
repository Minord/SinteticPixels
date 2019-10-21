
import unittest

import numpy as np

from SinteticPixels.img.img import Image

from SinteticPixels.operations import expand

import pdb

class TestExpand(unittest.TestCase):

    def test_expand(self):

        data = np.random.rand(32,32,1)
        gray_image = Image(data, 'image1')

        data2 = data > .5
        binary_image = Image(data2, 'image2')

        data3 = np.random.rand(32,32,3)
        rgb_image = Image(data3, 'image3')
        
        expanded_image = expand.expand_image(binary_image, left = 2, right= 2, top = 2, down= 2)

        expanded_image = expand.expand_image(gray_image, left = 5, right= 2, top = 2, down= 2)

        expanded_image = expand.expand_image(rgb_image, left = 5, right= 2, top = 2, down= 2)