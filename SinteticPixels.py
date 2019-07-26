import numpy as np
import cv2
import matplotlib.pyplot as plt
from SinteticPixels import Show
from SinteticPixels import GrayGeneration
from SinteticPixels import GenerationBinary
from SinteticPixels import GrayOperations
from SinteticPixels import BinaryOperations

#Load Img
img = cv2.imread("img/rgb/T2.png", cv2.IMREAD_GRAYSCALE)
#To binary
biimage = BinaryOperations.RGB2binary_img(img)
#Outline
outlineImg = BinaryOperations.getBorderPixels(biimage)
#Gaussian
gausianImg = GrayOperations.kernelGaussianOperation(biimage, 7)

renderImg = GrayOperations.resizeImgforPixelPerfectGray(gausianImg, 5)
cv2.imshow("image", renderImg)
cv2.waitKey(0)
renderImg = GrayOperations.resizeImgforPixelPerfectGray(biimage, 5)
cv2.imshow("image", renderImg)
cv2.waitKey(0)

#this is the algorimt.

#convert to binary #DONE
#getOutline #DONE

#getRandomPoints
#getGaussian
#GrowPixelsPath
#BrushOverPath
#UnionBinary
