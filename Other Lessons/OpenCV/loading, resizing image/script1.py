import cv2

img=cv2.imread('galaxy.jpg', 0)

resized_image=cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))
cv2.imshow('Galaxy', resized_image)
cv2.imwrite('resized_galaxy.jpg', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()