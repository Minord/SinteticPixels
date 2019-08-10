import numpy as np

class img:

	def __init__(self, img_data = None, img_type = None, channels_type = None, indexed_colors = None):

		self.img_data = img_data

		#handle img type image
		if img_data == None:
			self.img_data = np.zeros((16,16)) #create a emply image in case lack of data

		#get the np array shape
		img_shape = self.img_data.shape
		#num of chanells 1 for inizilizate
		self.num_channels = 1
		#if the img_data has more than 1 channel
		if len(img_shape) > 2:
			self.num_channels[2] = 1

		#resolve the type of the image
		self.channels_type = channels_type
		if channels_type == None:
			if self.img_data.dtype is np.int32:
				self.channels_type = "int"
			elif self.img_data.dtype is np.float64:
				self.channels_type = "float"
			elif self.img_data.dtype is np.bool:
				self.channels_type = "bool"
		#inizializete img_type
		self.img_type = img_type
		#infering img type.
		if img_type == None:

			if self.num_channels == 1:
				#clasify it like a gray-scale image or binary. 
				#self.img_type = "gray-scale"
				#0-1 float or 0 - 255 int
				if self.channels_type == "bool":
					self.img_type = "binary"
				elif indexed_colors != None:
					self.img_type = "indexed"

					#TODO: implement the indexed save information
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
					indexed to rgb - to gray-
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
	#general for convertion
	def get_top_scale(self):
		if self.channels_type == "int":
			return 255
		elif self.channels_type == "float":
			return 1
		return 0

	def get_np_type(channels_type):
		if channels_type == "int":
			return np.int32
		elif channels_type == "float":
			return np.float64
		elif channels_type == "float":
			return np.bool
		return None

	#converters for gray

	#gray to gray - alpha, gray to  rgb, gray to rgba, gray to bgr gray to binary, gray to indexed
	def gray_to_gray_alpha(self, img_data): #test it
		width, heigth = img_data.shape
		new_img_data = np.zeros((heigth, width, 2), dtype = get_np_type())

		new_img_data[:,:,0] = img_data
		new_img_data[:,:,1] = np.full(img_data.shape, get_top_scale(), dtype = get_np_type())

		return new_img_data

	def gray_to_rgb(self, img_data): # test it
		width, heigth = img_data.shape
		new_img_data = np.zeros((heigth, width, 3), dtype = get_np_type())

		new_img_data[:,:,0] = img_data
		new_img_data[:,:,1] = img_data
		new_img_data[:,:,2] = img_data

		return new_img_data

	def gray_to_rgba(self, img_data): #test it
		width, heigth = img_data.shape
		new_img_data = np.zeros((heigth, width, 4), dtype = get_np_type())

		new_img_data[:,:,0] = img_data
		new_img_data[:,:,1] = img_data
		new_img_data[:,:,2] = img_data
		new_img_data[:,:,3] = np.full(img_data.shape, get_top_scale(), dtype = get_np_type())

	def gray_to_brg(self, img_data):
		return gray_to_rgb(img_data) #this is because is indiferent

	def gray_to_binary(self, img_data, min_value_to_white):
		#TODO - search the way for doing it
		new_img_data = np.zeros((img_data.shape))

	def gray_to_indexed(self, img_data, gray_values_to_index):
		#TODO - search the way for doing it
		pass
		
	#converters for gray-alpha

	#gray alpha to gray, gray alpha to rgb, gray alpha to rgba, gray alpha to bgr, gray alpha to indexed

	#converters for rgb

	#rgb to gray, rgb to gray alpha, rgb to rgba, rgb to bgr, rgb to binary, rgb to indexed 

	#converters for rgba

	#rgba to gray, rgba to gray alpha, rgba to rgb, rgba to bgr, rgba to binary, rgb to indexed

	#converters for bgr

	#bgr to gray, bgr to gray alpha, bgr to rgb, bgr to rgba, bgr to binary, bgr to indexed

	#converters for binary

	#binary to gray, binary to gray alpha, binary to rgb, binary to rgba, binary to bgr, binary, to indexed

	#converters for indexed

	#indexed to gray, indexed to gray alpha, indexed to rgb, indexed to rgba, indexed to bgr, indexed to binary


#i had to analizies how to make the handle of the image data format initalization.
#what up wee whant to make this for example. is 255 - int 

#prodria generalizar segun el caso pues pues en 5 de los 7 casos aplicaria esto
#unicamente seria el cambio de canales.
#otro punto es observer que para dejar 

#parece que si elaboro esta clase de esta forma va a tomar un 
#trabajar gigantesco de semanas XD