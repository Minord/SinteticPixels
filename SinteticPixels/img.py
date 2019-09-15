import numpy as np
import pdb
import cv2

class img:

	def __init__(self, img_data = None, img_type = None, channels_type = None, indexed_colors = None):
		self.img_data = img_data

		#handle img type image
		if img_data is None: 
			self.img_data = np.zeros((16,16)) #create a emply image in case lack of data

		#get the np array shape
		img_shape = self.img_data.shape
		#num of chanells 1 for inizilizate
		self.num_channels = 1
		#if the img_data has more than 1 channel
		if len(img_shape) > 2:
			self.num_channels = img_shape[2]

		#resolve the type of the image
		self.channels_type = channels_type
		if channels_type is None:
			if self.img_data.dtype == 'int32':
				self.channels_type = "int"
			elif self.img_data.dtype == 'float':
				self.channels_type = "float"
			elif self.img_data.dtype == 'bool':
				self.channels_type = "bool"
		#inizializete img_type
		self.img_type = img_type
		#infering img type.
		if img_type is None:

			if self.num_channels == 1:
				#is bool type
				if self.channels_type == "bool":
					self.img_type = "binary"
				#if we have indexed_colors parameter defined set it like indexed image
				elif indexed_colors is not None:
					self.img_type = "indexed"
					
					#check the ndarray type is correct
					if self.channels_type == 'int':
						self.indexed_colors = indexed_colors
					else:
						#error: if we dont have de correct ndarray for indexed
						assert self.channels_type != 'int', 'channels_type needs to be int type ndarray, for indexed_colors'
				#if the data type is int or float the image is in gray-scale 
				elif self.channels_type == "int" or self.channels_type == "float":
					self.img_type = "gray-scale"
				else:
					print("Warring: something is bad with channels_type")

			if self.num_channels == 2:
				#clasify it like a gray-scale-alpha image
				if self.channels_type == "int" or self.channels_type == "float":
					self.img_type = "gray-scale-alpha"
				else:
					print("Warring: something is bad with channels_type")

			if self.num_channels == 3:
				#clasify it like a rgb image
				if self.channels_type == "int" or self.channels_type == "float":
					self.img_type = "rgb"
				else:
					print("Warring: something is bad with channels_type")

			if self.num_channels == 4:
				#clasify it like a rgba image
				if self.channels_type == "int" or self.channels_type == "float":
					self.img_type = "rgba"
				else:
					print("Warring: something is bad with channels_type")

		elif img_type == "gray-scale":
			#pseudocodigo
			"""
			if num_channels = 1
				if bool
					 convert bool to gray
				elif idexed.
					indexed to rgb -to gray-
				else.
					is gray

			if num_channels = 2.
				#delete one channel
			if num_channnels = 3
				#conver rgb to gray
			if num_channels = 4
				#conver rgba to gray
			"""

		elif img_type == "gray-scale-alpha":

			#pseudocodigo
			"""
				if num_channels = 1
					add one channel of alpha
				elif nun_channels = 2
					if int or float:
						is a gray-scale-alpha
					else:
						not correct np type
				elif num_channels 3
					conver rgb to gray
				elif num_channels 4:
					first 3 chanels to gray an add the alpha
			"""
			
		elif img_type == "rgb":

			#pseudocodigo
			"""

			"""

		elif img_type == "rgba":

			#pseudocodigo
			"""
			
			"""

		elif img_type == "bgr":

			#pseudocodigo
			"""
			
			"""

		elif img_type == "binary":

			#pseudocodigo
			"""
			
			"""

		elif img_type == "indexed":
		
			#pseudocodigo
			"""
			
			"""

		#end of constructor
	#misselaneus fuctions
	@staticmethod
	def get_top_scale(channels_type):
		if channels_type == "int" or channels_type == np.int32:
			return 255
		elif channels_type == "float" or channels_type == np.float64:
			return 1
		return 0
	
	@staticmethod
	def get_np_type(channels_type):
		if channels_type == "int":
			return np.int32
		elif channels_type == "float":
			return np.float64
		elif channels_type == "bool":
			return np.bool
		return None

	#converters for gray

	#gray to gray - alpha, gray to  rgb, gray to rgba, gray to bgr gray to binary, gray to indexed
	@staticmethod
	def gray_to_gray_alpha(img_data):
		width, heigth = img_data.shape
		new_img_data = np.zeros((heigth, width, 2), dtype = img_data.dtype)

		new_img_data[:,:,0] = img_data	
		new_img_data[:,:,1] = np.full(img_data.shape, img.get_top_scale(img_data.dtype), dtype = img_data.dtype)

		return new_img_data

	@staticmethod
	def gray_to_rgb(img_data):
		width, heigth = img_data.shape
		new_img_data = np.zeros((heigth, width, 3), dtype = img_data.dtype)

		new_img_data[:,:,0] = img_data
		new_img_data[:,:,1] = img_data
		new_img_data[:,:,2] = img_data

		return new_img_data

	@staticmethod
	def gray_to_rgba(img_data):
		width, heigth = img_data.shape
		new_img_data = np.zeros((heigth, width, 4), dtype = img_data.dtype)

		new_img_data[:,:,0] = img_data
		new_img_data[:,:,1] = img_data
		new_img_data[:,:,2] = img_data
		new_img_data[:,:,3] = np.full(img_data.shape, img.get_top_scale(img_data.dtype), dtype = img_data.dtype)

		return new_img_data

	@staticmethod
	def gray_to_bgr(img_data):
		return img.gray_to_rgb(img_data) #this is because is indiferent

	@staticmethod
	def gray_to_binary(img_data, min_value_to_white):
		new_img = img_data >= (min_value_to_white * img.get_top_scale(img_data.dtype))
		return new_img
		
	
	@staticmethod				  
	def gray_to_indexed(img_data, cut_values):
		img_levels = []

		top = img.get_top_scale(img_data.dtype)

		#generate a list of binariy imagenes for caculate the levels 
		for val in cut_values:
			img_levels.append(img_data >= (val * top))
		img_levels.append(img_data > 0)

		#pass binary to int
		for level in img_levels:
			level = level.astype(img.get_np_type('int'))

		final_img = np.zeros(img_data.shape , dtype = img.get_np_type('int'))

		#sum all layer for get the final image
		for level in img_levels:
			final_img += level

		return final_img
	
	#converters for gray-alpha

	#gray alpha to gray, gray alpha to rgb, gray alpha to rgba, gray alpha to bgr, gray alpha to indexed
	@staticmethod
	def gray_alpha_to_gray(img_data): #test it
		heigth, width, _ = img_data.shape
		new_img = np.zeros((heigth, width), dtype = img_data.dtype)
		new_img = img_data[:,:,1]
		return new_img

	@staticmethod
	def gray_alpha_to_rgb(img_data): #test it
		new_img = img.gray_alpha_to_gray(img_data)
		new_img = img.gray_to_rgb(new_img)
		return new_img

	@staticmethod
	def gray_alpha_to_rgba(img_data): #test it
		new_img = img.gray_alpha_to_gray(img_data)
		new_img = img.gray_to_rgba(new_img)
		return new_img

	@staticmethod
	def gray_alpha_to_bgr(img_data): #test it
		new_img = img.gray_alpha_to_gray(img_data)
		new_img = img.gray_to_bgr(new_img)
		return new_img

	@staticmethod
	def gray_alpha_to_binary(img_data, min_value_to_white): #test it
		new_img = img.gray_alpha_to_gray(img_data)
		new_img = img.gray_to_binary(new_img, min_value_to_white)
		return new_img

	@staticmethod
	def gray_alpha_indexed(img_data, cut_values): #test it
		new_img = img.gray_alpha_to_gray(img_data)
		new_img = img.gray_to_indexed(new_img, cut_values)
		return new_img

	#converters for rgb

	#rgb to gray, rgb to gray alpha, rgb to rgba, rgb to bgr, rgb to binary, rgb to indexed 
	@staticmethod
	def rgb_to_gray(img_data): #test it
		a = 0.2989
		b = 0.5870
		c = 0.1140
		new_img = img_data[:,:,0] * a + img_data[:,:,1] * b + img_data[:,:,2] * c
		
		return new_img

	@staticmethod
	def rgb_to_gray_alpha(img_data):  #test it
		heigth, width, _ = img_data.shape
		
		new_img = np.zeros((heigth, width, 2), dtype = img_data.dtype)

		new_img[:,:,0] = img.rgb_to_gray_alpha(img_data)
		new_img[:,:,1] = np.full((heigth, width), img.get_top_scale(img_data.dtype), dtype = img_data.dtype)

		return new_img

	@staticmethod
	def rgb_to_rgba(img_data):  #test it
		heigth, width, _ = img_data.shape
		
		new_img = np.zeros((heigth, width, 4), dtype = img_data.dtype)

		new_img[:,:,0:2] = img_data
		new_img[:,:,3] = np.full((heigth, width), img.get_top_scale(img_data.dtype), dtype = img_data.dtype)

		return new_img

	@staticmethod
	def rgb_to_bgr(img_data):  #test it
		new_img = np.zeros(img_data.shape,  dtype = img_data.dtype)

		new_img[:,:,0] = img_data[:,:,2]
		new_img[:,:,1] = img_data[:,:,1]
		new_img[:,:,2] = img_data[:,:,0]
		
		return new_img

	@staticmethod
	def rgb_to_binary(img_data, rgb_value):  #test it
		heigth, width, _ = img_data.shape

		new_img = np.zeros((heigth, width),  dtype = img.get_np_type('bool'))

		img_data = img_data.astype(np.int32)

		new_img = img_data[:,:,0] == rgb_value[0] / divisor_control
		new_img = np.logical_and(new_img, img_data[:,:,1] == rgb_value[1])
		new_img = np.logical_and(new_img, img_data[:,:,2] == rgb_value[2])

		return new_img

	@staticmethod
	def rgb_to_indexed(img_data, color_index):  #test it
		heigth, width, _ = img_data.shape

		new_img = np.zeros((heigth, width),  dtype = img.get_np_type('int'))

		img_data = img_data.astype(np.int32)
		isColor = lambda cond, index: index if cond else 0

		for x, y in zip(width, heigth):
			for i, color in enumerate(color_index):
			r = color[0] 
			g = color[1]
			b = color[2]
			pixel_color = img_data[y,x,:]
			color_concide = pixel_color[0] == r and  pixel_color[1] == g and  pixel_color[2] == b
			new_img[y, x] = isColor(color_concide, i+1)

		return new_img

	#converters for rgba

	#rgba to gray, rgba to gray alpha, rgba to rgb, rgba to bgr, rgba to binary, rgb to indexed

	@staticmethod
	def rgba_to_gray(img_data):  #test it
		heigth, width, _ = img_data.shape
		new_img = rgb_to_gray(img_data[:,:,0:2])
		return new_img

	@staticmethod
	def rgba_to_gray_alpha(img_data):  #test it
		heigth, width, _ = img_data.shape
		new_img = rgb_to_gray_alpha(img_data[:,:,0:2])
		return new_img

	@staticmethod
	def rgba_to_rgb(img_data):  #test it
		heigth, width, _ = img_data.shape
		new_img = img_data[:,:,0:2]
		return new_img

	@staticmethod
	def rgba_to_bgr(img_data):  #test it
		heigth, width, _ = img_data.shape
		new_img = rgb_to_bgr(img_data[:,:,0:2])
		return new_img

	@staticmethod
	def rgba_to_binary(img_data, rgb_value):  #test it
		heigth, width, _ = img_data.shape
		new_img = rgb_to_binary(img_data[:,:,0:2], rgb_value)
		return new_img

	@staticmethod
	def rgba_to_indexed(img_data, color_index):  #test it
		heigth, width, _ = img_data.shape
		new_img = rgb_to_indexed(img_data[:,:,0:2], color_index)
		return new_img

	#converters for bgr
	#bgr to gray, bgr to gray alpha, bgr to rgb, bgr to rgba, bgr to binary, bgr to indexed

	@staticmethod
	def bgr_to_gray(img_data):  #test it
		return rgb_to_gray(bgr_to_rgb(img_data))


	@staticmethod
	def bgr_to_gray_alpha(img_data):  #test it
		return rgb_to_gray_alpha(bgr_to_rgb(img_data))

	@staticmethod
	def bgr_to_rgb(img_data):  #test it
		new_img = np.zeros(img_data.shape, dtype = img_data.dtype)
		new_img[:,:,0] = img_data[:,:,2]
		new_img[:,:,1] = img_data[:,:,1]
		new_img[:,:,2] = img_data[:,:,0]
		return new_img

	@staticmethod
	def bgr_to_rgba(img_data):  #test it
		return rgb_to_rgba(bgr_to_rgb(img_data))

    @staticmethod
	def bgr_to_binary(img_data, rgb_value):  #test it
		return rgb_to_binary(bgr_to_rgb(img_data), rgb_value)

	@staticmethod
	def bgr_to_indexed(img_data, color_index):  #test it
		return rgb_to_indexed(bgr_to_rgb(img_data), color_index)

	#converters for binary

	#binary to gray, binary to gray alpha, binary to rgb, binary to rgba, binary to bgr, binary, to indexed

	@staticmethod
	def binary_to_gray(img_data):  #test it
		return img_data.astype(np.int32) * 255

	@staticmethod
	def binary_to_gray_alpha(img_data):  #test it
		return gray_to_gray_alpha(binary_to_gray(img_data))

	@staticmethod
	def binary_to_rgb(img_data):  #test it
		return gray_to_rgb(binary_to_gray(img_data))

	@staticmethod
	def binary_to_rgba(img_data):  #test it
		return gray_to_rgba(binary_to_gray(img_data))

	@staticmethod
	def binary_to_bgr(img_data):  #test it
		return gray_to_bgr(binary_to_gray(img_data))

	@staticmethod
	def binary_to_indexed(img_data):  #test it
		#this is the most interesting

	#converters for indexed

	#indexed to gray, indexed to gray alpha, indexed to rgb, indexed to rgba, indexed to bgr, indexed to binary

	@staticmethod
	def indexed_to_gray(img_data):  #test it
		pass

	@staticmethod
	def indexed_to_gray_alpha(img_data): #test it
		pass

	@staticmethod
	def indexed_to_rgb(img_data):  #test it
		pass

	@staticmethod
	def indexed_to_rgba(img_data):  #test it
		pass

	@staticmethod
	def indexed_to_bgr(img_data):  #test it
		pass
	
	@staticmethod
	def indexed_to_binary(img_data):  #test it
		pass

#hoow shit is true i can made a bridge img type. Fuckkkkkkk
#480 lines to the trash