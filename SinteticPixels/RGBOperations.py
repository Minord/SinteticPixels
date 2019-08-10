import numpy as np

def gray_to_rgb(gray_img):
	height, width = gray_img.shape
	newimg = np.zeros((height, width, 3))
	for i in range(3):
		newimg[:, :, i] = gray_img
	return newimg

#this is not tested it methosd not work
def replace_color(img, original_color, new_color, chanel_type = "rgb"):
	print(img.shape)
	newimg = img
	height, width, chanels = newimg.shape  #probability the chanels are in bgr

	f_color_original = original_color
	f_color_new = new_color

	if chanel_type == "rgb":
		f_color_original = original_color[::-1]
		f_color_new = new_color	[::-1]

	for i in range(width):
		for j in range(height):
			if img[j,i,0] == f_color_original[0] \
				and img[j,i,1] == f_color_original[1] \
				and img[j,i,2] == f_color_original[2]:

				newimg[j,i,:] = np.array([f_color_new[0], f_color_new[1], f_color_new[2]]) #it fail
	return newimg

#this method not work				
def overImg(img1, img2, color_tranparent=(0,0,0)):
	if not img1 == img2:
		print("Error the images has to have the same dimensions")
		return None
	newimg = img1
	height, width, chanels = newimg.shape

	bgr_color_tranparent = color_tranparent[::-1]  #pass to rgb color to bgr

	for i in range(width):
		for j in range(height):
			if not newimg[j,i,0] == bgr_color_tranparent[0] \
				and newimg[j,i,1] == bgr_color_tranparent[1] \
				and newimg[j,i,2] == bgr_color_tranparent[2]:

				newimg[j,i,:] = img2[j,i,:]
	return newimg