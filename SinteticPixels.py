import numpy as np
import cv2
import matplotlib.pyplot as plt
from SinteticPixels import Show
from SinteticPixels import GrayGeneration
from SinteticPixels import GenerationBinary
from SinteticPixels import GrayOperations

img = cv2.imread("img/binary/SD6.png", cv2.IMREAD_GRAYSCALE)

Show.plotImg(img)
Show.plotImg(GrayOperations.kernelLinearOperation(img, 7))

