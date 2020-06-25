from scipy.ndimage import binary_fill_holes
# from imagerie.imagerie import binary_fill_holes
from imagerie.operations import img_as_float, img_as_uint
from PIL import Image
import numpy as np
import cv2


gray = Image.open('running_mask_8.jpg').convert('L')

gray = img_as_uint(gray) * 255
# _, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
#
# im_floodfill = thresh.copy()
#
# h, w = thresh.shape[:2]
# mask = np.zeros((h+2, w+2), np.uint8)
#
# cv2.floodFill(im_floodfill, mask, (0, 0), 255)
#
# im_floodfill_inv = cv2.bitwise_not(im_floodfill)
#
# out = thresh | im_floodfill_inv

im_floodfill = binary_fill_holes(gray)

gray = Image.fromarray(im_floodfill).convert('L')
gray.show()
