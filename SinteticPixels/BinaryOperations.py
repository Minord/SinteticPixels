import random

import numpy as np
import cv2

from SinteticPixels import Utils as utils

def widenPixels(img, brush):
	"""Do widen white pixels and return a new image"""
	heigth, width = img.shape
	newImg = np.zeros((heigth, width))
	brush_heigth, brush_width = brush.shape
	#Calcular pivote

	PivotVec =  np.array([(brush_heigth - 1)/2 , (brush_width - 1)/2], np.int32)

	for i in range(0, width):
		for j in range(0, heigth):
			if img[j,i] == 255:
				#Stampar patron -parece que sera complicado
				for k in range(-PivotVec[1],PivotVec[1] + 1):
					for n in range(-PivotVec[0],PivotVec[0] + 1):
						if i + k >= 0 and i + k < width and j + n >= 0 and j + n < heigth:
							if  brush[n+PivotVec[0], k+PivotVec[1]] == 255:
								newImg[j+n,i+k] = 255 #work only solve it
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

def applyPixelsMask(img, imgmask):#probability not work
	heigth, width = img.shape
	newImg = cv2.bitwise_and(img, img, mask = imgmask)
	return newImg

def union(img1, img2, *argv):
	newimg = img1 + img2
	for img in argv:
		newimg = newimg + img
	return newimg

def interception(img1, img2, *argv): #probability not work
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
		lowerColorGray = 1
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

def randomSelectedPixels(img, probability = 0.5):
	newimg = np.zeros(img.shape)
	heigth, width = img.shape

	def randFuc(probability):
		if random.random() > probability:
			return 0
		else:
			return 255

	for x in range(width):
		for y in range(heigth):
			if img[y, x] != 0:
				newimg[y, x] = randFuc(probability)
	return newimg

	#not work so good but it is enoung to start
def followingGausianGradient(pointsimg, gaussianimg, length = 2): 
	newimg = np.zeros(pointsimg.shape)
	heigth, width = pointsimg.shape

	for x in range(width):
		for y in range(heigth):
			if pointsimg[y, x] != 0:
				#if we are in this point we start a path
				newx = x
				newy = y
				for l in range(length):
					newimg[newy, newx] = 255
					#in this point i have to chek the minor value araund
					found = False
					newDirection = np.array([0,0])
					minorValue = gaussianimg[newy, newx]

					for subx in range(-1,2):
						for suby in range(-1,2):
							if not (subx == 0 and suby == 0):
								if utils.isLegalArrayIndex((newy + suby, newx + subx), gaussianimg.shape):
									if gaussianimg[newy + suby, newx + subx] < minorValue:
										minorValue = gaussianimg[newy + suby, newx + subx]
										newDirection = np.array([suby, subx])
										found = True
					if found:
						newx += newDirection[1]
						newy += newDirection[0]
					else:
						break
	return newimg
					