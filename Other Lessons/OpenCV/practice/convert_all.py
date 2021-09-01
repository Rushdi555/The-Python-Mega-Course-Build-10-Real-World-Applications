import cv2
import glob
from pathlib import Path

images = glob.glob("original/*.jpg")

for image in images:
    img=cv2.imread(image, 0)
    re=cv2.resize(img, (100,100))
    name = image[9:]
    cv2.imshow('Hey', re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite('resized/'+'resized_'+name, re)
