import numpy as np
import cv2
import matplotlib.pyplot as plt

from SinteticPixels import Show
from SinteticPixels import GrayGeneration
from SinteticPixels import GenerationBinary
from SinteticPixels import GrayOperations
from SinteticPixels import BinaryOperations
from SinteticPixels import LoadImg
from SinteticPixels import RGBOperations
from tests import test

test.test_all()

img = cv2.imread("img/amins/Tree/TopLeafs.png", cv2.IMREAD_GRAYSCALE)
frames = LoadImg.cutSpriteSheet(img, 200, 200)

leafting_frames = []
for frame in range(2):
	leafting_frames.append(GenerationBinary.LeafShapes(frames[frame]))
	print("frame done")

print(leafting_frames[0].shape)
img1 = RGBOperations.gray_to_rgb(leafting_frames[0])
#img2 = cv2.cvtColor(leafting_frames[1],cv2.COLOR_GRAY2RGB)

img1 = RGBOperations.replace_color(img1, original_color=(255,255,255), new_color=(75,105,46))

Show.plotImg(img1)
cv2.imshow("i", img1)
cv2.waitKey(2000)
cv2.destroyAllWindows()

