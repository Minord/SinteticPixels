import numpy as np
import matplotlib.pyplot as plt
from SinteteticPixels import vectorField as vf


def plotVector2DField(vectorField):
	originsField = vf.vectorField2DOrigins(vectorField)
	plt.quiver(originsField[:,:,0], originsField[:,:,1], vectorField[:,:,0], vectorField[:,:,1], color=['r','b','g'], scale=50)
	plt.show()