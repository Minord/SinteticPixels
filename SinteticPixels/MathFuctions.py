from math import exp
import numpy as np

def bidimencionalGaussian(x, y, x0 = 0, y0 = 0, sigmaX = 1, sigmaY = 1, a=1):
	return a * exp(-((pow(x-x0, 2.0)/(2*pow(sigmaX, 2.0)))+(pow(y-y0, 2.0)/(2*pow(sigmaY, 2.0)))))

def bidimencionalGaussian_np(x, y, x0 = 0, y0 = 0, sigmaX = 1, sigmaY = 1, a=1):
	xf = (x-x0) ** 2
	yf = (y-y0) ** 2
	xd = 2*(sigmaX ** 2)
	yd = 2*(sigmaY ** 2)
	return a * np.exp(-( (xf / xd) + (yf / yd)))