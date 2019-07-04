import numpy as np
import cv2

def getCircleBrushUnpair(radio):
	radioControl = radio
	if radio < 0:
		print ('El radio no puede ser negativo')
		radio = 0
	diameter = 2*radioControl+1
	real_radio = diameter/2

	brush = np.zeros((diameter, diameter))

	for i in range(0,diameter):
		for j in range(0,diameter):
			corPoint = np.array([real_radio, real_radio], np.float);
			arrayPoint = np.array([i,j], np.float)
			testPoint = corPoint -arrayPoint
			if pow(testPoint[0],2) + pow(testPoint[1],2) <= pow(real_radio+.2,2):
				brush[i,j]=1;
			else:
				brush[i,j]=0;
	return brush

def perlinNoiseGen(image_size, layersDimensions):
	finalImg = np.zeros(image_size)
	heigth, width = image_size
	ratio = float(width) / float(heigth)
	for i in layersDimensions:
		if ratio >= 1:
			x = int((ratio * i[0]))
			y = int(i[0])
		else:
			ratio = 1 / ratio
			x = int(i[0])
			y = int((ratio * i[0]))
		rm = np.random.rand(y, x)
		finalImg += cv2.resize(rm, (image_size[1], image_size[0]), interpolation = cv2.INTER_CUBIC)*i[1]
	return finalImg