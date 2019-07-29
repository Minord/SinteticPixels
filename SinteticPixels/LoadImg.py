import cv2
import numpy as np

def cutSpriteSheet(img, width, height):
	img_height, img_width = img.shape #this only works for 1 chanel imgs
	
	x = int(img_width / width)
	y = int(img_height / height)

	imgs = []

	for i in range(x):
		for j in range(y):
			imgs.append(img[j*height:(j+1)*height, i*width:(i+1)*width])
	return imgs
		
	