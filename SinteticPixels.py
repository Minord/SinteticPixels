import numpy as np
import cv2
import matplotlib.pyplot as plt
from SinteticPixels import Show
from SinteticPixels import GrayGeneration
from SinteticPixels import GenerationBinary
from SinteticPixels import GrayOperations
from SinteticPixels import BinaryOperations


img = cv2.imread("img/rgb/T2.png", cv2.IMREAD_GRAYSCALE)

leafingimg = GenerationBinary.LeafShapes(img)

renderImg = GrayOperations.resizeImgforPixelPerfectGray(leafingimg, 5)

cv2.imshow("image", renderImg)
cv2.waitKey(0)
