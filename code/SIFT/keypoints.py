import matplotlib.pyplot as plt
import cv2 

#reading image
img1 = cv2.imread('../lean.png')  
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

#keypoints
sift = cv2.SIFT_create()
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)

img_1 = cv2.drawKeypoints(gray1,keypoints_1,img1)
plt.imshow(img_1)
plt.waitforbuttonpress(0)
print(len(descriptors_1));
