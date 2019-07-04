import numpy as np
import cv2 

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
	img_horizon = getBorderPixels(img)
	img_wided = widenPixels(img_horizon, getCircleBrushUnpair(border_size)) 
	img_masked = applyPixelsMask(img_wided, img)
	return img_masked
