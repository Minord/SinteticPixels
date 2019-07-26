import numpy as np
import cv2

def widenPixels(img, brush):

	heigth, width = img.shape
	newImg = np.zeros((heigth, width))
	brush_heigth, brush_width = brush.shape
	#Calcular pivote

	PivotVec =  np.array([(brush_heigth - 1)/2 , (brush_width - 1)/2], np.int32)

	for i in range(0, width):
		for j in range(0, heigth):
			if img[j,i] == 1:
				#Stampar patron -parece que sera complicado
				for k in range(-PivotVec[1],PivotVec[1] + 1):
					for n in range(-PivotVec[0],PivotVec[0] + 1):
						if i + k >= 0 and i + k < width and j + n >= 0 and j + n < heigth:
							if  brush[n+PivotVec[0], k+PivotVec[1]] == 1:
								newImg[j+n,i+k] = 1 #work only solve it
	return newImg

def	getBorderPixels(img):
	heigth, width = img.shape
	newImg = np.zeros((heigth, width))

	for i in range(0, width):
		for j in range(0, heigth):
			if img[j,i] == 0:
				if i-1 >= 0:
					if img[j,i-1] != 0:
						newImg[j,i] = 1
						continue
				if i+1 < width:
					if img[j,i+1] != 0:
						newImg[j,i] = 1
						continue
				if j-1 >= 0:
					if img[j-1,i] != 0:
						newImg[j,i] = 1
						continue
				if j+1 < heigth:
					if img[j+1,i] != 0:
						newImg[j,i] = 1
						continue
	return newImg

def applyPixelsMask(img, imgmask):
	heigth, width = img.shape
	newImg = cv2.bitwise_and(img, img, mask = imgmask)
	return newImg

def union(img1, img2, *argv):
	newimg = cv2.bitwise_or(img1, img2)
	for img in argv:
		newimg = cv2.bitwise_or(newimg, img)
	return newimg

def interception(img1, img2, *argv):
	newimg = cv2.bitwise_and(img1, img2)
	for img in argv:
		newimg = cv2.bitwise_and(newimg, img)
	return newimg

def negative():
	pass #TODO: interception images fuctions

def diference():
	pass #TODO: interception images fuctions

def RGB2binary_img(img, img_type='gray-scale', lowerColor = (255,255,255), upperColor = (255,255,255)):
	if(img_type == 'gray-scale'):
		lowerColorGray = 255
		upperColorGray = 255
		if type(lowerColor) is int:
			lowerColorGray = lowerColor
		if type(upperColor) is int:
			upperColorGray = upperColor
		newimg = cv2.inRange(img, lowerColorGray, upperColorGray)
		return newimg
		
	elif(img_type =='rgb'):
		newimg = cv2.inRange(img, lowerColor[::-1], upperColor[::-1])
		return newimg
	elif(img_type =='bgr'):
		newimg = cv2.inRange(img, lowerColor, upperColor)
		return newimg
	print("Error: img_type not accepted")
	return None
	