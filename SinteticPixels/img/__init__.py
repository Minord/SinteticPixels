#this is the image module of the proyect the propourse of this module
#is create classes for handle the img types. basic image operations

#well i have to descrive firts is the psilosofy of this modole gona be.

#give a object what can be use for representate images and their information


#What are the general capabilities?

#	GET A GENERAL OBJECT TO REPRESENT ANY IMAGE.

#	CREATE A UNIVERSAL FUCTIONS FOR OPERATE OVER 
#	IMG DATA IN ANY IMAGE TYPE WITH THE IMG TYPE LIMITS
#	-SUM IMAGES.
#	-MULTIPY IMAGES BY AN SCALAR.
#	-ALL NUMPY FUCTIONS.
#	-FOR LOOPS x, y information.
#	define it more.

#	CAN TRANSLATE ANY IMAGE TYPE TO ANOTHER EFICIENTLY

#	CAN SAVE AND LOAD THE IMGS EASILY

#create a type img object with the convercion protocols
#and the rules folowing by they for some operations.






#img buffer - a collections of images.
	#all the images are the same

#img object
	#header
	#data

	#load
	#save

#basic operations


	#updatepixels() it update a set of pixels whith defined cordinates.

#  //this object represents the propierties of the image.
#header object
	#name
	#color_type.
	#has alpha channel.
	#scales of pixels.
	#dtype of pixels.
	#color chanels.
	#color space.

	#int
	#float
	#bool

	#tags.

#data object
	#size
	#dtype
		
	#update pixels()
	#execute_np_fuction()

#convetion methods.
	#convertions into img types.


#for example this declarations if here can help mor make my code more 


#convetion FUCTIONS
#for each type of image is needed declare 2 functions (IMG_TYPE)_to_conv and conv_to_(IMG_TYPE)

class img_header():
	def __init__(img_type, img_name, alpha = False): 
		self.img_type = img_type
		self.alpha = alpha
		self.img_name = img_name
		self.complete_img_name = complete_name()

	def complete_name(self):
		return '{}_{}'.format(self.img_name, self.img_type['name'])

	def has_alpha(self):
		return self.alpha

	def can_have_alpha(self):
		return self.img_type['alpha']

class img_data():
	def __init__(data):
		self.data = data
		self.size = 0
		self.channels = 0
		self.dtype = 0

class universal_operations():
	pass


class indexed_operations():
	pass