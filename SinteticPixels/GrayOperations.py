import numpy as np
import cv2 
from SinteticPixels import BinaryOperations as bo
from SinteticPixels import GenerationBinary as genbin
from SinteticPixels import GrayGeneration as gengray

def resizeImgforPixelPerfectGray(img, zoom):
	control_zoom = zoom
	if zoom < 1:
		zoom = 1
	heigth, width  = img.shape
	img_rezised = cv2.resize(img, (width*control_zoom,heigth*control_zoom), interpolation = cv2.INTER_NEAREST)
	return img_rezised

def growWithBorders(img, growVector):
	xp1 = growVector[0]
	xp2 = growVector[1]
	yp1 = growVector[2]
	yp2 = growVector[3]

	heigth, width = img.shape
	newImg = np.zeros((heigth + yp1 + yp2, width + xp1 + xp2))
	heigth2, width2 = newImg.shape

	for i in range(0, width2):
		for j in range(0, heigth2):
			if i >= xp1 and i < width2-xp2:
			   if j >= yp1 and j < heigth2-yp2:
				    newImg[j, i] = img[j - yp1, i - xp1]
	return newImg

def genInnerBorder(img, border_size):
	img_horizon = bo.getBorderPixels(img)
	img_wided = bo.widenPixels(img_horizon, getCircleBrushUnpair(border_size)) 
	img_masked = bo.applyPixelsMask(img_wided, img)
	return img_masked

#noth, south, east, etc and diagonal directions - this not work
def kernelLinearOperation(img, n, direction="diagonal-down"):
	newimg = np.zeros(img.shape)

	kernel = (gengray.genGaussianKernel(n) / n**2) *3

	newimg = cv2.filter2D(img, -1, kernel)

	return newimg

def kernelGaussianOperation(img, kernel_size):
	kernel = (gengray.genGaussianKernel(kernel_size))
	newImg = cv2.filter2D(img, -1, kernel) #apply a convolutional operation
	return newImg

