import numpy as np

from SinteticPixels import MathFuctions as mf

def genGaussianKernel(n):
	kernel_size = n
	if n % 2 == 0:
		kernel_size += 1
		print ("For a kernel is only accepted unpair numbers")

	kernel_array = np.zeros((kernel_size, kernel_size))

	for x in range(kernel_size):
		for y in range(kernel_size):
			convFactor = (2.0/float(kernel_size-1))
			xc = convFactor * x - 1
			yc = convFactor * y - 1
			kernel_array[y,x] = mf.bidimencionalGaussian(xc, yc, 0, 0, .5,.5,1)

	return kernel_array / np.sum(kernel_array)