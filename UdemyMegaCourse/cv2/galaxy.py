import cv2
from matplotlib import pyplot as plt

img = cv2.imread('galaxy.jpg', 0)
plt.imshow(img)
plt.show()

cv2.imshow('Galaxy', img)
cv2.waitkey(5000)
cv2.destroyAllWindows()
