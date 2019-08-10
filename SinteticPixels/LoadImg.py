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
		
def jointSpriteSheet(imgs, width, height):
	spriteimg = np.zeros((height, width * len(imgs)))

	i = 0
	for img in imgs:
		if not img.shape == (height, width):
			print("Error: Image " + str(i) + " not coinside the size")
			continue
		spriteimg[0:height-1, width*i : (width*(i+1))-1] = img[0:height-1, 0:width-1]
		i += 1
	return spriteimg