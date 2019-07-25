import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.image as mpimg	

from SinteticPixels import VectorFields as vf
from SinteticPixels import MathFuctions as mf


def plotVector2DField(vectorField):
	originsField = vf.vectorField2DOrigins(vectorField)
	plt.quiver(originsField[:,:,0], originsField[:,:,1], vectorField[:,:,0], vectorField[:,:,1], color=['r','b','g'], scale=50)
	plt.show()

def plot3DGaussianFuction():
	#How i can make this firts is i had to create the window
	#Calculate the sets
	x = np.linspace(-1, 1, 50)
	z = np.linspace(-1, 1, 50)
	X, Z = np.meshgrid(x,z)
	Y = mf.bidimencionalGaussian_np(X,Z, 0, 0, .5, .5, 1)

	fig = plt.figure()
	ax = plt.axes(projection='3d')

	ax.contour3D(X, Z, Y, 50, cmap='binary')
	ax.set_xlabel('x')
	ax.set_ylabel('z')
	ax.set_zlabel('y')
	plt.show()

def plotImg(arrayimg):
	imgplot = plt.imshow(arrayimg)
	plt.show()