import numpy as np

def DecreseFunction(x):
	return pow(abs(x)+1,-1.3)

def isLegalArrayIndex(index, shape):
	isLegal = False
	if index[1] >= 0 and index[1] < shape[1] and index[0] >= 0 and index[0] < shape[0]:
		isLegal = True
	return isLegal