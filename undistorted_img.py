import cv2
import numpy as np
import scipy.io as scio

# Load the .mat file that contains the LUT
mat_contents = scio.loadmat("./wave_000006.mat")

# Load the image that you want to correct
image = cv2.imread("./wave_distorted_000006.jpg")
h, w  = image.shape[:2]
x, y  = np.meshgrid(np.arange(w), np.arange(h))

# Retrieve the u and v displacement maps from the .mat file
u = mat_contents['u']
v = mat_contents['v']

undistorted_image = cv2.remap(image, (x - u).astype(np.float32), (y - v).astype(np.float32), cv2.INTER_LINEAR)
result            = cv2.hconcat([image, undistorted_image])

cv2.imwrite("distorted_image_and_undistorted_image.jpg", result)
cv2.imshow('distorted_image_and_undistorted_image', result)
cv2.waitKey(0)

