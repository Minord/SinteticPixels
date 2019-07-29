import numpy as np
import cv2
import matplotlib.pyplot as plt
from SinteticPixels import Show
from SinteticPixels import GrayGeneration
from SinteticPixels import GenerationBinary
from SinteticPixels import GrayOperations
from SinteticPixels import BinaryOperations
from SinteticPixels import LoadImg


img = cv2.imread("img/amins/Tree/BackLeafs.png", cv2.IMREAD_GRAYSCALE)

frames = LoadImg.cutSpriteSheet(img, 200, 200)

#leafting
leafting_frames = []
for frame in frames:
	leafting_frames.append(GenerationBinary.LeafShapes(frame))
	print("frame done")

resized_frames = []
#resized
for frame in leafting_frames:
	resized_frames.append(GrayOperations.resizeImgforPixelPerfectGray(frame, 2))

f = 0
while True:
	cv2.imshow("image", resized_frames[f])
	f += 1
	if f >= len(resized_frames):
		f = 0
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break