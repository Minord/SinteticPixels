import numpy as np

from PIL import Image

import pdb
class conv_img():
	
	def __init__(self, img_data):
		h, w, c  = img_data.shape 

		if not (c == 3 or c == 4):
			raise Exception('img_data channels num is not accepted')

		if not (img_data.dtype == np.float64):
			raise Exception('img_data dtype is not np.float64')

		self.img_data = img_data

	def get_data(self, alpha = False):
		h, w, c  = self.img_data.shape

		if c == 3:
			if alpha:					
				new_img_data = np.full((h, w,4), 255, np.float64)
				new_img_data[:,:,0:3] = self.img_data 
				return new_img_data
			else:
				return self.img_data
		elif c == 4:
			if alpha:
				return self.img_data
			else:
				return self.img_data[:,:,0:3]


def setInConvRange(data, actual_scale):
	n, m = actual_scale
	return (data-n)*(255.0/m-n)

def inRangeFromConv(data, desire_scale):
	n, m = desire_scale
	return data*((m-n)/255) + n

class img():

	def __init__(self):
		pass

	#gray_scale convertions
	@staticmethod
	def gray_scale_to_conv(img_data, actual_scale):
		new_img_data = np.full(img_data.shape + (3,), 255, dtype = np.float64)
		img_data = setInConvRange(img_data.astype(np.float64), actual_scale)
		new_img_data[:,:,0] = img_data
		new_img_data[:,:,1] = img_data
		new_img_data[:,:,2] = img_data
		return conv_img(new_img_data)
	
	@staticmethod
	def conv_to_gray_scale(conv_data, desire_scale, np_type):
		np_conv_data = conv_data.get_data()
		r = 0.2989
		g = 0.5870
		b = 0.1141
		new_img_data = (np_conv_data[:,:,0] * r + np_conv_data[:,:,1] * g + np_conv_data[:,:,2] * b)
		return inRangeFromConv(new_img_data, desire_scale).astype(np_type)

	#gray_scale_alpha convertions
	@staticmethod
	def gray_scale_alpha_to_conv(img_data, actual_scale):
		w, h, c = img_data.shape
		new_img_data = np.full((w, h, 4), 255, dtype = np.float64)
		img_data = setInConvRange(img_data.astype(np.float64), actual_scale)
		temp_layer = img_data[:,:,0]
		new_img_data[:,:,0] = temp_layer
		new_img_data[:,:,1] = temp_layer
		new_img_data[:,:,2] = temp_layer
		new_img_data[:,:,3] = img_data[:,:,1]
		return conv_img(new_img_data)

	@staticmethod
	def conv_to_gray_scale_alpha(conv_data, desire_scale, np_type): #WTF 
		np_conv_data = conv_data.get_data(alpha=True)
		r = 0.2989
		g = 0.5870
		b = 0.1141
		gray_img_data = (np_conv_data[:,:,0] * r + np_conv_data[:,:,1] * g + np_conv_data[:,:,2] * b)

		new_img_data = np.zeros(gray_img_data.shape + (2,), np_type)

		new_img_data[:,:,0] = inRangeFromConv(gray_img_data, desire_scale).astype(np_type)
		new_img_data[:,:,1] = np.full(gray_img_data.shape, desire_scale[1], np_type)

		return new_img_data

	#rgb convertions
	@staticmethod
	def rgb_to_conv(img_data, actual_scale):
		new_img_data = np.full(img_data.shape, 255, dtype = np.float64)
		new_img_data = setInConvRange(img_data.astype(np.float64), actual_scale)
		return conv_img(new_img_data)

	@staticmethod
	def conv_to_rgb(conv_data, desire_scale, np_type):
		return setInConvRange(conv_data.get_data() , desire_scale).astype(np_type)

	#rgba convertions
	@staticmethod
	def rgba_to_conv(img_data, actual_scale):
		new_img_data = np.full(img_data.shape, 255, dtype = np.float64)
		new_img_data = setInConvRange(img_data.astype(np.float64), actual_scale)
		return conv_img(new_img_data)

	@staticmethod
	def conv_to_rgba(conv_data, desire_scale, np_type):
		return setInConvRange(conv_data.get_data(alpha=True) , desire_scale).astype(np_type)

	#bgr convertions
	@staticmethod
	def bgr_to_conv(img_data, actual_scale):
		new_img_data = np.full(img_data.shape, 255, dtype = np.float64)
		new_img_data[:,:,0] = img_data[:,:,2]
		new_img_data[:,:,1] = img_data[:,:,1]
		new_img_data[:,:,2] = img_data[:,:,0]
		new_img_data = setInConvRange(new_img_data, actual_scale)
		return conv_img(new_img_data)

	@staticmethod
	def conv_to_bgr(conv_data, desire_scale, np_type):
		img_data = conv_data.get_data()
		temp_img = np.full(img_data.shape, 255, dtype = np.float64)
		temp_img[:,:,0] = img_data[:,:,2]
		temp_img[:,:,1] = img_data[:,:,1]
		temp_img[:,:,2] = img_data[:,:,0]
		return setInConvRange(temp_img , desire_scale).astype(np_type)

	#binary convertions
	@staticmethod
	def binary_to_conv(img_data):
		new_img_data = np.full(img_data.shape + (3,), 255, dtype = np.float64)
		temp_layer = setInConvRange(img_data.astype(np.float64) ,(0,1)) 
		new_img_data[:,:,0] = temp_layer
		new_img_data[:,:,1] = temp_layer
		new_img_data[:,:,2] = temp_layer
		return conv_img(new_img_data)

	@staticmethod
	def conv_to_binary(conv_data, white_value = (255, 255, 255)):
		img_data = conv_data.get_data()
		r, g, b = white_value
		img_r_considence = img_data[:,:,0] == r
		img_g_considence = img_data[:,:,1] == g
		img_b_considence = img_data[:,:,2] == b

		return np.logical_and(np.logical_and(img_r_considence, img_g_considence), img_b_considence)

	#indexed convertions
	@staticmethod
	def indexed_to_conv(img_data, color_indexed):
		new_comv_img_data = np.zeros(img_data.shape + (3,), np.float64)

		for index, color in color_indexed.items(): #color_indexed is a dictionary
			r, g, b =  color.value
			
			temp_binary = (img_data == index).astype(np.float64)
			new_comv_img_data[:,:,0] = temp_binary * r
			new_comv_img_data[:,:,1] = temp_binary * g
			new_comv_img_data[:,:,2] = temp_binary * b
			
		return conv_img(new_comv_img_data)

	@staticmethod
	def conv_to_indexed(img_data, color_indexed = 0):
	
		pil_img = Image.fromarray(img_data.astype('uint8'), 'RGB')
		pil_img.convert('P', color_indexed)
		new_img = np.array(pil_img).astype(np.int32)

		return new_img