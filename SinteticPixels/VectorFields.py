import numpy as np
from SinteticPixels import Utils as utils

#It has a decents perfonmace.
def randomVectorField(dimensions):
	return (np.random.rand(dimensions[0], dimensions[1], 2) -.5) * 5 

def vectorField2DOrigins(vectorField):
	heigth, width, _vd = vectorField.shape
	originsVec = np.zeros(vectorField.shape)
	for x in range(0, width):
		for y in range(0, heigth):
			originsVec[x, y] = [float(x),float(y)]
	return originsVec

def sumVectors(vectorField, origins, actualPos):
	fVec = np.array((0.0,0.0))
	heigth, width, _d = origins.shape
	for x in range(0, width):
		for y in range(0, heigth):
			fVec += vectorField[y, x] * utils.DecreseFunction(np.linalg.norm(actualPos - origins[y, x]))
	return fVec

def interpolateVector2DField(vectorField, newVectorDimensions):
	newVec = np.zeros((newVectorDimensions[0], newVectorDimensions[1], 2))

	origins = vectorField2DOrigins(vectorField)

	conv_heigth = float(newVectorDimensions[0]) / float(vectorField.shape[0])
	conv_width = float(newVectorDimensions[1]) / float(vectorField.shape[1])

	for x in range(0, newVectorDimensions[1]):
		for y in range(0, newVectorDimensions[0]):
			xf = x / conv_heigth
			yf = y / conv_width
			actualPos = np.array((xf,yf))
			newVec[y, x] = sumVectors(vectorField, origins, actualPos)
	return newVec

def deformationByVectorField(img, vecField):
	newImg = np.zeros(img.shape)
	img_heigth, img_width = img.shape
	for x in range(0, img_width):
		for y in range(0, img_heigth):
			img_value = 1
			index = [int(vecField[y, x, 1])+ y, int(vecField[y, x, 0])+ x]
			if utils.isLegalArrayIndex(index, img.shape):
				img_value = img[index[0],index[1]]
			newImg[y, x] = img_value

	return newImg